class MyClass:
    __hidden_variable = 0

    def add(self, increment):
        self.__hidden_variable += increment
        print(self.__hidden_variable)


myObject = MyClass()
myObject.add(2)
myObject.add(5)
print(myObject.__hidden_variable)
