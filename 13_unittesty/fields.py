def rectangle(a, b):
    numeric_types = (int, float)
    if not isinstance(a, numeric_types) or not isinstance(b, numeric_types):
        raise ValueError('Bok musi być wartością numeryczną!')

    return a * b


def triangle(a, h):
  return 0.5 * a * h

def trapezoid(a,b,h):
    return (a + b) * h * 0.5

def main():
    print(rectangle(10, 5) == 50)
    print(triangle(10, 5) == 25)
    print(rectangle(10, "lalala"))


if __name__ == "__main__":
    main()