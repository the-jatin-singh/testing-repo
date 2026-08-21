def greet(name):
    if not name:
        name = "there"
    return f"Hello, {name}!"


def add(a, b):
    return a + b


def multiply(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("multiply() only supports int or float arguments")
    return a * b


if __name__ == "__main__":
    print(greet("world"))
    print(add(2, 3))
    print(multiply(2, 3))
