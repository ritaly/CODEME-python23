# Stwórz zmienną password. Hasło powinno składać z liter i cyfr,
# zwierać conajmniej 1 małą literę,
# 1 dużą literę i mieć długość conajmniej 8 znaków,
# Poinformuj użytkownika, jeśli wpisane hasło jest nie poprawne.
# Wyświetl różne komunikaty w zależności od rodzaju błędu

password = "haslooooooO1"

# jesli za krótkie
if len(password) < 8:
    print('Password too short')
# jesli nie ma cyfry
if password.isalnum() and password.isalpha():
    print('Password needs at least one digit')
# jesli nie ma litery
if password.isalnum() and password.isdigit():
    print('Password needs at least one letter')
# jesli nie ma małej litery
if password.islower():
    print('Password needs at least 1 upper letter')

# jeśli nie ma dużej litery
if password.isupper():
    print('Password needs at least 1 lower letter')

print(f'super [not] secure password here -> {password}')