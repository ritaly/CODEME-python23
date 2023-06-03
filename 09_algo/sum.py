def sum_natural_for(n):
    sum_nr = 0

    for i in range(1, n+1):
        sum_nr += i
        print(i, '-> suma:', sum_nr)

    return  sum_nr


def sum_natural_while(n):
    sum_nr = 0

    while n >= 0:
        print(n, ' suma:', sum_nr)
        sum_nr += n
        n -= 1
    return sum_nr



# sum rekurencyjne
def sum_me(n):
    if n == 1:
        return 1
    else:
        return n + sum_me(n-1)



# print(sum_natural_for(10))
# print(sum_natural_while(10))

print(sum_me(10))