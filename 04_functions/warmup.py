def add_books(number):
    library = {}

    for i in range(number):
        title = input("Podaj tytuł książki:")
        review = input("Jak oceniasz książkę od 1-10")
        library[title] = review

    return library

# ---- glowna czesc
counter = int(input("Ile książek chcesz dodać"))
data = add_books(counter)
print(data)
# shelf = list(data.items())
# print(shelf)