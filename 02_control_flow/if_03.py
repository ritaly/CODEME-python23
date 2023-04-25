review1 = int(input('Book review 1 (1-10) -> '))
review2 = int(input('Book review 2 (1-10) -> '))
review3 = int(input('Book review 3 (1-10) -> '))

average = (review1 + review2 + review3)/3
average = round(average, 3)
print(average)

if average >= 7:
    print("very good")
elif average >= 4:
    print("not interesting")
else:
    print("bad")