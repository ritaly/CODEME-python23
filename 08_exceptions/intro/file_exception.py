fopen = open('myfile.txt', 'r')

try:
    x = fopen.read()
    print(x)
    x = int(x)
    # raise Exception('I'm rebel!'')
except Exception as mess:
    print("Jakies błędy ->", mess)

finally:
    fopen.close()
    print("Zamknieto tryb odczytu pliku")