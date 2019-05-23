
# simple Dog class
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        """
        Prints Woof when called
        """
        print("{} says Woof!".format(self.name))




