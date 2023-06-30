class Person(object):
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def print_self_details(self):
        print("My name is {} {}".format(self.firstname, self.lastname))


john = Person("John", "Doe")
print(john.firstname, john.lastname)
