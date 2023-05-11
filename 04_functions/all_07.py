# Napisz program, który na podstawie numeru karty odpowie czy ma doczynienia z Visą, MasterCard, a może AmericanExpress.
# Co wiemy o tych numerach tych kart?
# All Visa card numbers start with a 4. New cards have 16 digits. Old cards have 13.
#
# MasterCard numbers either start with the numbers 51 through 55 or with the numbers 2221 through 2720. All have 16 digits.
#
# American Express card numbers start with 34 or 37 and have 15 digits.
#

def is_card_number(num):
    if num.isdigit():
        return True
    else:
        return False


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


number = get_card_number()
print('💳 :', number)
# 2 func -> czy to jest karta visa

# 3. func ->  czy to master card

# 4 func -> czy to american express
