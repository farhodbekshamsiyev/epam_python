from typing import List, Tuple


def replace_symbol(string):
    """
    Task 4.1
    Implement a function which receives a string and replaces all `"` symbols
    with `'` and vise versa.
    :param string:
    :return: string
    """
    res = ''
    for i in string:
        if i == "'":
            res += '"'
        elif i == '"':
            res += "'"
        else:
            res += i
    return res


def palindrome(string) -> bool:
    """
    Task 4.2
    Write a function that check whether a string is a palindrome or not.
    :param string:
    :return: bool
    """
    for i in range(len(string) // 2):
        if string[i] != string[len(string) - i - 1]:
            return False
    return True


def str_split(string, char):
    """
    Task 4.3
    :param string
    :param char:
    :return: List[str]
    """
    result = []
    carry = ''
    for i in string:
        if i == char or not char:
            if not char:
                carry += i
                result.append(carry)
            else:
                result.append(carry)
            carry = ''
        else:
            carry += i
    return result


def split_by_index(s: str, indexes: List[int]) -> List[str]:
    """
    Task 4.4
    :param s:
    :param indexes:
    :return:List[str]
    """
    result = []
    carry = ''
    j = 0
    for i in range(len(s)):
        carry += s[i]
        if (i + 1) == indexes[j]:
            result.append(carry)
            carry = ''
            j += 1
        if j == len(indexes):
            result.append(s[i:])
            break
    return result


def get_digits(num: int) -> Tuple[int]:
    """
    Task 4.5
    :param num:
    :return: Tuple[int]
    """
    return tuple(int(x) for x in str_split(str(num), ''))

#
# b = get_digits(87178291199)
# print(b)


def get_shortest_word(s: str) -> str:
    """
    Task 4.6
    :param s:
    :return: str
    """
    res = str_split(s, ' ')
    nmax = ''
    for i in res:
        if len(i) > len(nmax):
            nmax = i
    return nmax


# a = get_shortest_word('Any pythonista like namespaces a lot.')
# b = get_shortest_word('Python is simple and effective!')
# print(a, b)


