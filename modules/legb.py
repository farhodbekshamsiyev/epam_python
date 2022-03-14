import functools

a = "I am global variable!"


def enclosing_funcion():
    a = "I am variable from enclosed function!"

    def inner_function():
        # nonlocal a
        a = "I am local variable!"
        return a

    inner_function()

    return inner_function()
