class ThisClass:
    def __init__(self, variable_a, variable_b):
        self.variable_a = variable_a
        self.variable_b = variable_b

    def __repr__(self):
        return "Class a:%s b:%s" % (self.variable_a, self.variable_b)

    def __str__(self):
        return "From __str__(): a is %s, " \
            "b is %s" % (self.variable_a, self.variable_b)


c = ThisClass(123, 456)
print(c)  # calls __str__()
print([c])  # calls __repr__()
