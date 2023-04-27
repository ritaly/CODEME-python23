my_tuple = (3, 4, 5, 11, 34, 14, 2)

num = int(input('Podaj liczbe do sprawdzenia->'))

if num in my_tuple:
    # podaj index tego elementu
    print('Jest w krotce!')
    print(f'Numer {num} pod indexem ->', my_tuple.index(num))
else:
    print('Nie ma w krotce')