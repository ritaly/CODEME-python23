try:
    with open('text.txt', 'x') as file:
        file.write("Hello World")
except FileExistsError:
    print('Plik już istnieje ')