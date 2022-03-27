class Bird(object):
    """
    Task 4.4
    Create hierarchy out of birds.
    """

    # __slots__ = ['name']

    def __init__(self, name: str):
        self.name = name

    def fly(self):
        print(f'{self.name} bird can fly')

    def walk(self):
        print(f'{self.name} bird can walk')

    def __str__(self):
        return f'{self.name} can fly and walk'


class FlyingBird(Bird):
    # __slots__ = ['ration']

    def __init__(self, name: str, ration: str = 'grains'):
        super(FlyingBird, self).__init__(name)
        self.ration = ration

    def fly(self):
        print(f'{self.name} bird can fly')

    def walk(self):
        print(f'{self.name} bird can walk')

    def eat(self):
        print(f'It eats mostly {self.ration}')


class NonFlyingBird(object):
    # __slots__ = ['ration']

    def __init__(self, name: str, ration: str = 'fish'):
        self.bird = Bird(name)
        self.ration = ration

    def walk(self):
        print(f'{self.bird.name} bird can walk')

    def swim(self):
        print(f'{self.bird.name} bird can swim')

    def eat(self):
        print(f'It eats mostly {self.ration}')

    def __str__(self):
        print(f'{self.bird.name} can walk and swim')


class SuperBird(FlyingBird, NonFlyingBird):

    def __init__(self, name: str, ration: str = 'fish'):
        super(SuperBird, self).__init__(name, ration)

    def __str__(self):
        return f'{self.name} bird can walk, swim and fly'

# b = Bird("Any")
# b.walk()

# p = NonFlyingBird("Penguin", "fish")
# p.swim()
# p.fly()
# p.eat()

# c = FlyingBird("Canary")
# print(str(c))
# c.eat()

# s = SuperBird("Gull")
# print(str(s))
# s.eat()
