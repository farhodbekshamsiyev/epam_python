import csv
import modules
from modules import legb
from collections import Counter
from functools import cached_property, wraps


def sort_names(filename):
    """
    Task 4.1
    :param filename:
    :return:
    """
    sorted_names = open('data/sorted_names.txt', mode='w')
    with open(filename, mode='r') as file:
        lines = file.readlines()
        lines.sort()
        sorted_names.writelines(lines)
    sorted_names.close()


# sort_names('data/unsorted_names.txt')

def most_common_words(filename, number_of_words=3):
    """
    Task 4.2
    :param number_of_words:
    :param filename:
    :return:
    """
    ans = []
    b = []
    with open(filename, 'r') as file:
        for f in file:
            f = f.lower()
            ans += f.split()
        ans = [x.replace('.', '') for x in ans]
        ans = [x.replace(',', '') for x in ans]
        ans = sorted(list(Counter(ans).items()), key=lambda x: x[1])
        print(ans)
        return [x for x, y in ans[-number_of_words:]]


# print(most_common_words('data/lorem_ipsum.txt'))

def get_top_performers(file_path, number_of_top_students=5):
    """
    Task 4.3
    :param file_path:
    :param number_of_top_students:
    :return:
    """
    f = open('data/students_info.csv', 'w')
    fieldnames = ['student name', 'age', 'average mark']
    writer = csv.DictWriter(f, fieldnames=fieldnames)

    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        items = list(reader)
        items = sorted(items, key=lambda d: d['average mark'])
        info = sorted(items, key=lambda d: d['age'], reverse=True)
        writer.writerows(info)
        f.close()
        return [x['student name'] for x in items[-number_of_top_students:]]


# print(get_top_performers("data/students.csv"))


def look_through():
    """
    Task 4.4
    :return:
    """
    inner = legb.enclosing_funcion
    print(inner())


# look_through()

def remember_result(sm):
    """
    Task 4.5
    :param sm:
    :return:
    """
    result = None

    def wrapper(*args):
        nonlocal result
        print(f"Last result = '{result}'")
        result = sm(*args)
        return result

    return wrapper


@remember_result
def sum_list(*args):
    result = ""
    for item in args:
        result += str(item)
    print(f"Current result = '{result}'")
    return result


# sum_list("a", "b")
# sum_list("abc", "cde")
# sum_list(3, 4, 5)

def call_once(func):
    result = []

    @wraps(func)
    def wrapper(a, b):
        if not result:
            result.append(func(a, b))
        return result[0]

    return wrapper


@call_once
def sum_of_numbers(a, b):
    return a + b


# print(sum_of_numbers(13, 42))
# print(sum_of_numbers(999, 100))
# print(sum_of_numbers(134, 412))
# print(sum_of_numbers(856, 232))

# print(modules.mod_a)
