import random
import time
from contextlib import contextmanager, suppress
from functools import wraps


class Open:
    """
    Task 7.1
    """

    def __init__(self, filename: str, mode: str):
        self.file_name = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        try:
            self.file = open(self.file_name, self.mode)
            return self.file
        except FileNotFoundError:
            print(f'{self.file_name} does not exists')

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        if exc_type:
            print(exc_val)
        return True


# with Open('8data/lorem_ipsum.txt', 'r') as file:
#     print(file.readline())

@contextmanager
def opening(name, mode):
    """
    Task 7.2
    :param name:
    :param mode:
    :return:
    """
    file = None
    try:
        file = open(name, mode)
        yield file
    except FileNotFoundError:
        print("We had an error!")
    finally:
        # print('File closed')
        file.close()


# with opening('data/lorem_ipsum.txt', 'r') as filex:
#     print(filex.readline())


def context_decorator(open_f):
    """
    Task 7.3
    :param open_f:
    :return:
    """

    def decorator_open(func):
        @wraps(func)
        def wrapper():
            start = time.perf_counter()
            func()
            end = time.perf_counter()
            with open_f('log.txt', 'a+') as file:
                print(f'Execution time {end - start}', file=file)

        return wrapper

    return decorator_open


@context_decorator(opening)
def count_num():
    for i in range(100000):
        yield


# count_num()


def suppressing_exceptions(func):
    """
    Task 7.4
    :param func:
    :return:
    """

    @wraps(func)
    def wrapper():
        for a in range(1, 51):
            with suppress(ZeroDivisionError):
                b = func()
                ans = a // b
                with opening('log.txt', 'a+') as f:
                    print(f'result : {ans}', a, b, file=f)

    return wrapper


@suppressing_exceptions
def random_num():
    return random.randint(-2, 2)


# random_num()

class MyException(Exception):
    """
    Task 7.5
    """

    def __init__(self, msg: str, exc=0):
        self.message = msg
        super(MyException, self).__init__(msg)
        self.exception = exc

    def __str__(self):
        return f'{self.message} {self.exception}'


def is_even(num: int) -> bool:
    if num % 2 == 0:
        print(f'{num} is even')
        return True
    else:
        raise MyException(f'{num} is odd')


# is_even(4)

def eratosthenes(n):
    primes = list(range(2, n + 1))
    for i in primes:
        j = 2
        while i * j <= primes[-1]:
            if i * j in primes:
                primes.remove(i * j)
            j = j + 1
    return primes


def odd_primes(x):
    oddprimes = eratosthenes(x)
    oddprimes.remove(2)
    return oddprimes


def goldbach():
    """
    Task 7.6
    :return:
    """
    while True:
        N = input('Enter number  ')
        try:
            if N == 'q':
                print('Application is stopping')
                break
            elif isinstance(int(N), int):
                N = int(N)
                x, y = 0, 0
                result = 0
                try:
                    if N % 2 == 0 and N > 4:
                        prime = odd_primes(N)
                        while result != N:
                            for i in range(len(prime)):
                                if result == N:
                                    break
                                x = prime[i]
                                for j in range(len(prime)):
                                    y = prime[j]
                                    result = x + y
                                    if result == N:
                                        print(x, y)
                                        break
                    else:
                        raise MyException('Number should be even and higher than 4')
                except Exception:
                    raise MyException('Error')
            else:
                raise MyException('input should be either in or "q" symbol')
        except ValueError as ex:
            print(ex)


# goldbach()

class MySquareIterator:
    """
    Task 4.8
    """

    def __init__(self, lst):
        self.lst = lst
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == len(self.lst):
            raise StopIteration
        self.index += 1
        return self.lst[self.index - 1] ** 2


# lst = [1, 2, 3, 4, 5]
# itr = MySquareIterator(lst)
# for item in itr:
#     print(item, end=' ')


class EvenRange:
    """
    Task 4.9
    """

    def __init__(self, start, end):
        if start % 2 == 0:
            self.start = start
        else:
            self.start = start + 1
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < self.end:
            x = self.start
            self.start += 2
            return x
        else:
            raise StopIteration


# er1 = EvenRange(7, 11)
# print(next(er1))
# print(next(er1))
# print(next(er1))
# er2 = EvenRange(3, 14)
# for number in er2:
#     print(number)

def endless_generator():
    """
    Task 4.10
    :return:
    """
    x = 1
    while True:
        yield x
        x += 2


# gen = endless_generator()
# while True:
#     print(next(gen))


def endless_fib_generator():
    """
    Task 4.11
    :return:
    """
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b

# gen = endless_fib_generator()
# while True:
#     print(next(gen), end=' ')
