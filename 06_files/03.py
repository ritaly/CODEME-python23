def get_content():
    filename = input('Podaj nazwe pliku (bez rozszerzenia txt)')
    with open(f'{filename}.txt') as fopen:
        content = fopen.readlines()

    return content


def main():
    quotes = get_content()
    for id in range(5):
        print(quotes[id])


main()