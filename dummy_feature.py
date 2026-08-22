def multiply(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("multiply() only supports int or float arguments")
    return a * b


if __name__ == "__main__":
    print(multiply(2, 3))
