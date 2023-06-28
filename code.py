class Dog:
    # class attribute
    attribute = "mammal"

    # instance attribute
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("My name is {}".format(self.name))


# Driver code & instantiation
midnight_the_husky = Dog("Midnight")

midnight_the_husky.speak()
