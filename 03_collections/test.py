print('***********************************')
print('Zad3')

krotka = (93, 4, 5, 6, 7, 8, 9)

while True:
    try:
        num = int(input('podaj liczbe: '))
        break
    except ValueError:
        print('Zły typ.')

if num in krotka:
    print(f'{num} jest w krotce po numerem {krotka.index(num)}')
else:
    print('Nie jest w krotce')