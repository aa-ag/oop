class Dog:
    # class attribute
    attribute = "mammal"

    # instance attribute
    def __init__(self, name):
        self.name = name


# Driver code & instantiation
midnight_the_husky = Dog("Midnight")

print(f"{midnight_the_husky.name} is a {midnight_the_husky.attribute}")
