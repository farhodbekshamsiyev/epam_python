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

def foo(ints: List[int]) -> List[int]:
    """
    Task 4.7
    :param ints:
    :return:List[int]
    """
    mult = 1
    res = []
    for i in ints:
        mult *= i
    for i in range(len(ints)):
        res.append(mult // ints[i])
    return res


# print(foo([1, 2, 3, 4, 5]), foo([3, 2, 1]))


def get_pairs(lst: List) -> List[Tuple]:
    """
    Test 4.8
    :param lst:
    :return:List[Tuple]
    """
    if len(lst) < 2:
        return None
    a = ''
    res = []
    for i in lst:
        if a:
            res.append((a, i,))
        a = i
    return res


# print(get_pairs([1, 2, 3, 8, 9]))
# get_pairs(['need', 'to', 'sleep', 'more'])

def change_str_1(*strings):
    """
    Task 4.9-1
    :param strings:
    :return:char
    """
    in_str = 0
    strs = set(strings[0])
    for i in strs:
        for j in strings[1:]:
            if i not in j:
                in_str = 0
                break
            else:
                in_str = 1
        if in_str:
            return i


test_strings = ["hello", "world", "python", ]


# print(change_str_1(*test_strings))

def change_str_2(*strings):
    """
    Task 4.9-2
    :param strings:
    :return:set
    """
    return set(''.join(*strings))


# print(change_str_2(test_strings))

def change_str_3(*strings):
    """
    Task 4.9-3
    :param strings:
    :return:set
    """
    dict_s = {}
    ans = set()
    for i in strings:
        for j in set(i):
            if j not in dict_s:
                dict_s[j] = 1
            else:
                ans.add(j)
    return ans


# print(change_str_3(*test_strings))

def change_str_4(*strings):
    """
    Task 4.9-4
    :param strings:
    :return:list
    """
    first = change_str_2(strings)
    second = {'a', 'b', 'c', 'd', 'e', 'f',
              'g', 'h', 'i', 'j', 'k', 'l',
              'm', 'n', 'o', 'p', 'q', 'r',
              's', 't', 'u', 'v', 'w', 'x',
              'y', 'z'}

    return sorted(first ^ second)


# for i in range(26):
#     print('\'' + chr(ord('a') + i) + '\'' + ',', end=' ')
# print(change_str_4(*test_strings))

def generate_squares(n):
    """
    Task 4.10
    :param n:
    :return:dict
    """
    return {k: (k * k) for k in range(1, 6)}


# print(generate_squares(5))


def combine_dicts(*args):
    """
    Task 4.11
    :param args:
    :return:dict
    """
    ans = {}
    for dict_items in args:
        for item in dict_items.items():
            k, v = item
            if k not in ans:
                ans[k] = v
            else:
                ans[k] += v
    return ans


# dict_1 = {'a': 100, 'b': 200}
# dict_2 = {'a': 200, 'c': 300}
# dict_3 = {'a': 300, 'd': 100}
# print(combine_dicts(dict_1, dict_2, dict_3))
