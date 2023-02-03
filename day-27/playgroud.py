def add(*args):
    sum = 0
    for arg in args:
        sum += arg
    return sum

print(add(5, 4, 3))

def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)