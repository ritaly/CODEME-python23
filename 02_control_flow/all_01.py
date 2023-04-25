name = input('podaj imiona: ')
name_list = name.replace(" ", "").split(',')
for step in name_list:
    print('Hello ', step)
