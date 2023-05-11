# Napisz program, który na podstawie numeru karty odpowie czy ma doczynienia z Visą, MasterCard, a może AmericanExpress.
# Co wiemy o tych numerach tych kart?
# All Visa card numbers start with a 4. New cards have 16 digits. Old cards have 13.
#
# MasterCard numbers either start with the numbers 51 through 55 or with the numbers 2221 through 2720. All have 16 digits.
#
# American Express card numbers start with 34 or 37 and have 15 digits.

def is_card_number(num):
    return num.isdigit()

def get_card_number():
    while True:
        card_nr = input("Insert card number here ->")

        if is_card_number(card_nr):
            print("Yes, can be card number")
            break
        else:
            print("Nope! This is not card number")
            print("-- Try again! --")

    return card_nr


def is_visa(card_num):
    """Function that checks visa numbers"""
    if card_num[0] == '4' and (len(card_num) == 16 or len(card_num) == 13):
        return True
    else:
        return False


def is_mastercard(card_num):
    """Function that checks mastercard numbers"""
    start_condition = int(card_num[0:2]) in range(51, 56) or int(card_num[0:4]) in range(2221, 2721)

    if len(card_num) == 16 and start_condition:
        return True
    else:
        return False


def is_amex(card_num):
    """Function that checks amex numbers"""
    # American Express card numbers start with 34 or 37 and have 15 digits.
    if len(card_num) == 15 and card_num[0:2] in ('34', '37'):
        return True
    else:
        return False

# --- main part of the program

number = get_card_number()
print('💳 :', number)

if is_visa(number):
    print("This is Visa card number")
elif is_mastercard(number):
    print("This is MasterCard card number")
elif is_amex(number):
    print("This is AmericanExpress card number")
else:
    print("Unknown card number")

