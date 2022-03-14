from typing import Dict, Any


class CounterNum:
    """
    Task 4.1
    Implement a Counter class which optionally accepts
    the start value and the counter stop value.
    """
    __count = 0
    __max_count = 0

    def __init__(self, start: int = 0, stop: int = float('inf')):
        self.__count = start
        self.__max_count = stop

    def increment(self):
        if self.__count != self.__max_count:
            self.__count += 1
        if self.__count == self.__max_count:
            print('Maximal value is reached.')

    def get(self):
        return self.__count


# c = CounterNum(start=42)
# c.increment()
# print(c.get())
# c = CounterNum()
# c.increment()
# c.increment()
# print(c.get())

# c = CounterNum(start=42, stop=43)
# c.increment()
# c.increment()
# print(c.get())

class HistoryDict:
    dict_var = {}
    history = []

    def __init__(self, var: dict):
        self.dict_var = var
        self.history.append(*var)

    def set_value(self, key: str, val: Any):
        if len(self.dict_var) < 11:
            self.dict_var[key] = val
            self.history.append(key)
        else:
            temp = self.history.pop(0)
            del self.dict_var[temp]
            self.dict_var[key] = val
            self.history.append(key)

    def get_history(self):
        return self.history


# d = HistoryDict({"foo": 42})
# d.set_value("bar", 43)
# print(d.get_history())
atemp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
btemp = ['a', 'b', 'c', 'd', 'e', 'f',
         'g', 'h', 'i', 'j', 'k', 'l',
         'm', 'n', 'o', 'p', 'q', 'r',
         's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

d = ''


# x = set(btemp) ^ set(d)
# print(sorted(list(x)), len(x))


class Cipher:
    __alphabet = ['a', 'b', 'c', 'd', 'e', 'f',
                  'g', 'h', 'i', 'j', 'k', 'l',
                  'm', 'n', 'o', 'p', 'q', 'r',
                  's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    __cypher = []
    __key = []

    def __init__(self, keyword):
        res = []
        for i in keyword.lower():
            if i not in res:
                res.append(i)
        x = sorted(list(set(self.__alphabet) ^ set(res)))
        self.__cypher = res + x
        self.__key = res
        del res
        print(''.join(self.__alphabet))
        print(''.join(self.__cypher))

    def encode(self, text: str):
        res = ''
        for i in text.lower():
            if i in self.__cypher:
                res += self.__cypher[ord(i) - ord('a')]
            else:
                res += i
        print(res)

    def decode(self, text: str):
        res = ''
        for i in text.lower():
            if i in self.__cypher:
                index = self.__cypher.index(i)
                res += self.__alphabet[index]
            else:
                res += i
        print(res)


cipher = Cipher("crypto")
cipher.encode("Hello world")
cipher.decode("Fjedhc dn atidsn")
