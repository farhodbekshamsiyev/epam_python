from functools import total_ordering


@total_ordering
class Money(object):
    exchange_rate = {
        'GBP': 0.75,
        'EUR': 0.91,
        'CHF': 0.93,
        'CAD': 1.26,
        'AUD': 1.34,
        'SGD': 1.36,
        'BYN': 3.25,
        'CNY': 6.37,
        'JPY': 120.83,
        'USD': 1.00
    }

    def __init__(self, value: float, currency: str = 'USD'):
        self.val = value
        self.curr = currency
        self.in_usd = round(self.val / self.exchange_rate[currency], 2)

    def __eq__(self, other):
        return self.val == other.val

    def __ge__(self, other):
        return self.val >= other.val

    def __add__(self, other):
        if isinstance(other, Money):
            return Money((self.in_usd + other.in_usd) * self.exchange_rate[self.curr], self.curr)
        elif isinstance(other, (int, float)):
            return Money(self.val + other, self.curr)
        else:
            raise TypeError(f"sorry, don't know how to add by {type(other).__name__}")

    def __radd__(self, other):
        return self.__add__(other)

    def __mul__(self, other):
        if isinstance(other, Money):
            return Money((self.in_usd * other.in_usd) * self.exchange_rate[self.curr], self.curr)
        elif isinstance(other, (int, float)):
            return Money(self.val * other, self.curr)
        else:
            raise TypeError(f"sorry, don't know how to add by {type(other).__name__}")

    def __rmul__(self, other):
        return self.__mul__(other)

    def __repr__(self):
        return f'{self.val} {self.curr}'


x = Money(10, "BYN")
y = Money(11)  # define your own default value, e.g. “USD”
z = Money(12.34, "EUR")
print(z + 3.11 * x + y * 0.8)  # result in “EUR”
print(z + x * 3.11 + 0.8 * y)  # result in “EUR”

lst = [Money(10, "BYN"), Money(11), Money(12.01, "JPY")]
s = sum(lst)
print(s)  # result in “BYN”
