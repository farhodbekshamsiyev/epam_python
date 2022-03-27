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
