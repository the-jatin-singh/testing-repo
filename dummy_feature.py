def greet(name):
    if not name:
        name = "there"
    return f"Hello, {name}!"


def add(a, b):
    return a + b


if __name__ == "__main__":
    print(greet("world"))
    print(add(2, 3))
