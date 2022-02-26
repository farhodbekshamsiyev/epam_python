import math


def length_of_string(string):
    """
    Task 2.1
    Write a Python program to calculate the length
    of a string without using the `len` function.
    :param string:
    :return: num
    """
    counter = 0
    for _ in string:
        counter += 1

    return counter


def count_characters(string):
    """
    Task 2.2
    Write a Python program to count the number of characters
    (character frequency) in a string (ignore case of letters).
    :param string:
    :return: dictionary
    """
    dictionary = {}
    for i in string:
        if i not in dictionary:
            dictionary[i] = 1
        else:
            dictionary[i] += 1

    return dictionary


def get_unique_words(words):
    """
    Test 2.3
    :param words:
    :return: list
    """
    dictionary = {}
    for i in words:
        if i not in dictionary:
            dictionary[i] = 1

    return sorted(dictionary.keys())


def get_num_divisors(num):
    """
    Task 2.3
    Create a program that asks the user for a number and
    then prints out a list of all the [divisors]
    (https://en.wikipedia.org/wiki/Divisor) of that number.
    :param num:
    :return: list
    """
    divisor = 1
    divisor_list = []
    while divisor < int(math.sqrt(num)):
        if num % divisor == 0:
            divisor_list.append(divisor)
            divisor_list.append(num // divisor)
            divisor += 1

    return sorted(divisor_list)


def sort_dict_by_key(dictionary):
    """
    Task 2.4
    Write a Python program to sort a dictionary by key.
    :param dictionary:
    :return: list
    """
    return sorted(dictionary, key=lambda x: x[0])


def unique_dict_values(dict_list):
    """
    Task 2.5
    :param dict_list:
    :return: set
    """
    unique = set()
    for i in dict_list:
        for val in i.values():
            unique.add(val)

    return unique


def tuple_to_int(tup):
    """
    Task 2.6
    :param tup:
    :return: int
    """
    integer = 0
    for i in tup:
        integer = (integer + i) * 10

    return integer // 10


def multiplication_table(a, b, c, d):
    """
    Task 2.7
    :param a:
    :param b:
    :param c:
    :param d:
    :return: List[list]
    """
    # table = [[0] * (abs(c - d) + 2)] * (abs(a - b) + 2)
    table = [[0 for j in range((abs(c - d) + 2))] for i in range((abs(a - b) + 2))]

    for i in range(1, (abs(c - d) + 2)):
        table[0][i] = c + i - 1

    for i in range(1, (abs(a - b) + 2)):
        table[i][0] = a + i - 1

    for i in range(len(table)):
        for j in range(len(table[i])):
            if i > 0 and j > 0:
                table[i][j] = table[0][j] * table[i][0]
            # print(table[i][j], end=' ')
        # print()
    return table
