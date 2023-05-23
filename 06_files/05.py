filename = "./intro/pan_tadzio.txt"

with open(filename) as fopen:
    content = fopen.read()

content = content.replace(',', '').split()

longest_word = ''
for word in content:
    if len(word) > len(longest_word):
        print(word, '-', longest_word)
        print(len(word),'-',  len(longest_word))
        longest_word = word

print("Najdłuże słowo to ... ", longest_word)