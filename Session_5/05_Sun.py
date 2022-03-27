class Sun(object):
    """
    Task 4.6
    Implement singleton logic inside your custom class using a
    method to initialize class instance.
    """
    _instance = None

    # def __new__(cls, *args, **kwargs):
    #     if not Sun._instance:
    #         Sun._instance = super(Sun, cls).__new__(cls, *args, **kwargs)
    #     else:
    #         print('Class instantiated')

    def __init__(self):
        if not Sun._instance:
            Sun._instance = self
        else:
            print('Class instantiated')

    @staticmethod
    def inst():
        if not Sun._instance:
            Sun()
        return Sun._instance

# a = Sun.inst()
# b = Sun.inst()
# d = Sun()
# e = Sun()
# print(d._instance)
# print(e._instance)
# print(e is d)
# print(a, b)
# print(a is b)
