import bmi

def open_advice(filename):
    with open(f'{filename}.txt') as f:
        advice = f.read()

    return advice

def validate(value, type):
    limit = 600 if type == int else 2.8

    if isinstance(value, type) and value > limit:
        raise ValueError('Nieprawdopodobna wartość')


def get_input(message, type):
    while True:
        try:
            value = input(message)
            x = type(value)
            validate(x, type)
            return x

        except ValueError:
            print("Podano złe dane")

def main():
    w = get_input("Podaj wagę [kg] ", int)
    h = get_input("Podaj wzrost [m] ", float)

    result = bmi.calc_bmi(h, w)
    status = bmi.get_bmi_status(result)
    advice = open_advice(status)
    print(status.upper(), '***************')
    print(advice)

if __name__ == "__main__":
    main()