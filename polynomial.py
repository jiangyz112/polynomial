class X:
    def __init__(self):
        pass

    def __repr__(self):
        return "X"

    def evaluate(self, x):
        return x


class Int:
    def __init__(self, i):
        self.i = i

    def __repr__(self):
        return str(self.i)

    def evaluate(self, x):
        return self.i


class Add:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        return repr(self.p1) + " + " + repr(self.p2)

    def evaluate(self, x):
        return self.p1.evaluate(x) + self.p2.evaluate(x)


class Mul:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        if isinstance(self.p1, (Add, Sub, Mul, Div)):
            p1_repr = "( " + repr(self.p1) + " )"
        else:
            p1_repr = repr(self.p1)

        if isinstance(self.p2, (Add, Sub, Mul, Div)):
            p2_repr = "( " + repr(self.p2) + " )"
        else:
            p2_repr = repr(self.p2)

        return p1_repr + " * " + p2_repr

    def evaluate(self, x):
        return self.p1.evaluate(x) * self.p2.evaluate(x)


class Div:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        return "( " + repr(self.p1) + " ) / ( " + repr(self.p2) + " )"

    def evaluate(self, x):
        denominator = self.p2.evaluate(x)
        if denominator != 0:
            return self.p1.evaluate(x) / denominator
        else:
            raise ValueError("Division by zero")


class Sub:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        return "( " + repr(self.p1) + " ) - ( " + repr(self.p2) + " )"

    def evaluate(self, x):
        return self.p1.evaluate(x) - self.p2.evaluate(x)


# Example usage
poly = Add(Add(Int(4), Int(3)), Add(X(), Mul(Int(1), Add(Mul(X(), X()), Int(1)))))
print(poly)

# Evaluate the polynomial for x = -1
result = poly.evaluate(-1)
print(result)