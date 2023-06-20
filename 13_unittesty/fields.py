def is_numeric(*values):
    numeric_types = (int, float)

    for v in values:
        if not isinstance(v, numeric_types):
            raise ValueError(f'{v} musi być wartością numeryczną!')


def rectangle(a, b):
    numeric_types = (int, float)
    is_numeric(a, b)

    return a * b


def triangle(a, h):
    numeric_types = (int, float)
    is_numeric(a, h)

    return 0.5 * a * h

def trapezoid(a,b,h):
    numeric_types = (int, float)
    is_numeric(a, b, h)

    return (a + b) * h * 0.5

def main():
    print(rectangle(10, 5) == 50)
    print(triangle(10, 5) == 25)
    print(rectangle(10, "lalala"))


if __name__ == "__main__":
    main()