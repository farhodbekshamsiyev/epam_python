import csv
from collections import Counter
from functools import wraps

from modules import legb


def sort_names(filename):
    """
    Task 4.1
    Open file `data/unsorted_names.txt` in data folder. Sort the names and write them to a new file called
    `sorted_names.txt`. Each name should start with a new line as in the following example:
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
    Implement a function which search for most common words in the file.
    Use `data/lorem_ipsum.txt` file as a example.
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
    1) Implement a function which receives file path and returns names of top performer students
    2) Implement a function which receives the file path with srudents info and writes CSV student information
    to the new file in descending order of age.
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
    Look through file `modules/legb.py`.
    1) Find a way to call `inner_function` without moving it from inside of `enclosed_function`.
    2.1) Modify ONE LINE in `inner_function` to make it print variable 'a' from global scope.
    2.2) Modify ONE LINE in `inner_function` to make it print variable 'a' form enclosing function.
    :return:
    """
    inner = legb.enclosing_funcion
    print(inner())


# look_through()

def remember_result(sm):
    """
    Task 4.5
    Implement a decorator `remember_result` which remembers
    last result of function it decorates and prints it before next call.
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
    """
    Task 4.6
    Implement a decorator `call_once` which runs a function or method once
    and caches the result. All consecutive calls to this function should
    return cached result no matter the arguments.
    :param func:
    :return:
    """
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
