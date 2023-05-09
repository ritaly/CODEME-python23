# Napisać funkcję, która oblicza pole koła na podstawie zadanego promienia.
# pi * r^2

def calc_area(radius):
    pi = 3.14
    return pi * radius ** 2


r = int(input("Podaj promień -> "))
print("Pole koła = ", calc_area(r))