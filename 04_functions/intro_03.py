# Napisać funkcję, która przyjmuje listę liczb i zwraca sumę wszystki elementów na liście.

def sum_elements(items):
    result = 0
    for i in items:
        result += i

    return result
    # return sum(items)


summary = sum_elements([4, 6, 7])
print(summary)