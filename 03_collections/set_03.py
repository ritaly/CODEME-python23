 # 1. Utwórz 2 krotki.
tuple1 = (1, 2, 3, 4, 5, 6, 6)
tuple2 = (1, 1, 4, 5, 4, 4, 2)

 # 2. Następnie utwórz listę będącą połączeniem elementów o parzystym indeksie z pierwszej krotki,
 # a oraz nieparzystych elementów z drugiej.
tuples_to_list = list(tuple1[:: 2] + tuple2[1:: 2])

print(tuples_to_list)

# 3. Przekształć powstałą listę w set.

list_to_set = set(tuples_to_list)
print(list_to_set)
