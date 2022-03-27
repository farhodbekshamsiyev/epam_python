# atemp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# btemp = ['a', 'b', 'c', 'd', 'e', 'f',
#          'g', 'h', 'i', 'j', 'k', 'l',
#          'm', 'n', 'o', 'p', 'q', 'r',
#          's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#
# d = ''
# x = set(btemp) ^ set(d)
# print(sorted(list(x)), len(x))

class Cipher:
    """
    Task 4.3
    Implement The Keyword encoding and decoding for latin alphabet.
    The Keyword Cipher uses a Keyword to rearrange the letters in the alphabet.
    Add the provided keyword at the begining of the alphabet.
    """
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

# cipher = Cipher("crypto")
# cipher.encode("Hello world")
# cipher.decode("Fjedhc dn atidsn")
