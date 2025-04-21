class TestClass:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return TestClass(self.value + other.value)

    def __sub__(self, other):
        return TestClass(self.value - other.value)

    def __mul__(self, other):
        return TestClass(self.value * other.value)

    def __truediv__(self, other):
        return TestClass(self.value / other.value)

    def __floordiv__(self, other):
        return TestClass(self.value // other.value)

    def __mod__(self, other):
        return TestClass(self.value % other.value)

    def __pow__(self, other):
        return TestClass(self.value ** other.value)

    def __eq__(self, other):
        return self.value == other.value

    def __ne__(self, other):
        return self.value != other.value

    def __lt__(self, other):
        return self.value < other.value

    def __le__(self, other):
        return self.value <= other.value

    def __gt__(self, other):
        return self.value > other.value

    def __ge__(self, other):
        return self.value >= other.value

    def __repr__(self):
        return f"TestClass({self.value})"