class Number(object):
    def __init__(self, n):
        self.n = n


class First(Number):
    def __init__(self, n, as_string):
        self.as_string = as_string

        Number.__init__(self, n)

    def is_true(self):
        return False


class Second(Number):
    def __init__(self, n, as_string):
        self.as_string = as_string

        Number.__init__(self, n)

    def is_true(self):
        return True


if __name__ == "__main__":
    a_number = First(1, "One")
    print(a_number.is_true())

    another_number = Second(2, "Two")
    print(another_number.is_true())
