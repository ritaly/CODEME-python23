poem = """Szybko, zbudź się, szybko, wstawaj
Szybko, szybko, stygnie kawa
Szybko, zęby myj i ręce"""

poem = poem.lower().replace(",", "").split()
counting_word = {}

for word in poem:
    if word in counting_word:
        counting_word[word] += 1
    else:
        counting_word[word] = 1

for word, counter in counting_word.items():
    print("*", word, "-", counter)