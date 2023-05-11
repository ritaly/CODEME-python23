def get_card_number():
    while True:
        card_nr = input("Insert card number here ->")
        card_nr = card_nr.replace(" ", "")
        card_nr = card_nr.replace("-", "")

        if card_nr.isdigit():
            print("Yes, can be card number")
            break
        else:
            print("Nope! This is not card number")
            print("-- Try again! --")

    return card_nr


def is_visa(card_num):
    """Function that checks visa numbers"""
    return card_num[0] == '4' and (len(card_num) == 16 or len(card_num) == 13)
    # if card_num[0] == '4' and (len(card_num) == 16 or len(card_num) == 13):
    #     return True
    # else:
    #     return False


def is_mastercard(card_num):
    """Function that checks mastercard numbers"""
    start_condition = int(card_num[0:2]) in range(51, 56) or int(card_num[0:4]) in range(2221, 2721)

    return len(card_num) == 16 and start_condition
    # if len(card_num) == 16 and start_condition:
    #     return True
    # else:
    #     return False


def is_amex(card_num):
    """Function that checks amex numbers"""
    return len(card_num) == 15 and card_num[0:2] in ('34', '37')
    # if len(card_num) == 15 and card_num[0:2] in ('34', '37'):
    #     return True
    # else:
    #     return False


def main():
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

# --- main part of the program

main()


