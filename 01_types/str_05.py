# Palindrom to wyrażenie brzmiące tak samo czytane od lewej do prawej i od prawej do lewej np.:
# Kobyła ma mały bok.
# Pozwól użytkownikowi wprowadzić dowolne zdanie.
# Następnie sprawdź czy wprowadzone wyrażenie jest palindromem.

txt = input("Give me text here -> ")
txt = txt.replace(" ", "").upper()
print('Is text palindrom? ->',  txt == txt[::-1])

