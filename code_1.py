class Number(object):
    def __init__(self, n):
        self.n = n


class First(Number):
    def __init__(self, n, as_string):
        self.as_string = as_string

        Number.__init__(self, n)

    def print_details(self):
        print("First number inherited: {} {}".format(
            self.n, self.as_string
        ))


if __name__ == "__main__":
    a_number = First(1, "One")
    a_number.print_details()
