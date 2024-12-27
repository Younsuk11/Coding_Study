class Number:
    def __init__(self, val=0):
        self.val = val


def add(a: Number, b: Number) -> Number:
    c = Number
    c.val = a.val + b.val
    return c
