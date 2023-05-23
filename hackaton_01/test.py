def znajdz_klucz(slownik, wartosc):
    for klucz, wart in slownik.items():
        if wart == wartosc:
            return klucz
    return None

example = {'a': 1, 'b': 2, 'c': 3, 'd': 2, 'e': 2}
szukana_wartosc = 2

klucz = znajdz_klucz(example, szukana_wartosc)
print(klucz)