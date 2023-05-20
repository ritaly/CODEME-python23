# papier kamien nozyce
import random
# słownik wygrany: przegrany

WINNERS = {
    'k': ('n', 'j'),
    'n': ('p', 'j'),
    'p': ('k', 's'),
    'j': ('p', 's'),
    's': ('n', 'k')
}

CORRECT_VALUES = ['k', 'n', 'p', 'j', 's']

def get_comp_choice():
    return random.choice(CORRECT_VALUES)


def get_user_choice():
    while True:
        user_choice = input("""Podaj wartość:
                k - kamień
                n - nożyce
                p - papier
                j - jaszczuka
                s - Spock
        -> """)

        if user_choice in CORRECT_VALUES:
            break #return user_choice
        else:
            print('Nieprawidłowa wartość')
            print("--- spróbuj jeszcze raz! ---")

    return user_choice

def show_result(comp, user):
    if comp == user:
        print('Remis')
    elif comp in WINNERS[user]:
        print('Wygrana użytkownika')
    else:
        print('Wygrywa komputer')


def main():
    while True:
        comp = get_comp_choice()
        user = get_user_choice()
        print("-------WYBORY --------")
        print(f'komputer -> {comp} vs user -> {user}')
        show_result(comp, user)

        play_again = input("Czy chcesz zagrać ponownie? [T / N] -> ")

        if play_again.upper() == 'N':
            break

    print("*** Dzięki za grę! *** ")


main()