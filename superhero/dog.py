
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

    def sit(self):
        """
        Dog sits when called
        """
        print("{} is sitting now".format(self.name))

    def roll_over(self):
        """
        Dog Rolls over when called
        """
        print("{} is rolling over".format(self.name))



