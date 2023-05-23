import random

def get_content():
    with open('quotes.txt') as fopen:
        content = fopen.readlines()

    return content


def show(quote):
    print('Quote of the day is:')
    print()
    width = 60
    print('*' * width)
    print(quote.strip().center(width))
    print('*' * width)


def main():
    quotes = get_content()
    quote = random.choice(quotes)
    show(quote)

main()