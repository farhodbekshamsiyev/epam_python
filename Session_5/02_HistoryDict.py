from typing import Any


class HistoryDict:
    """
    Task 4.2
    Implement custom dictionary that will memorize 10 latest changed keys.
    Using method "get_history" return this keys.
    """
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
