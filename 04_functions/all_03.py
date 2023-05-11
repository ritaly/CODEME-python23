# Nie korzystając z funkcji wbudowanej max(),
# napisz funkcję znajdującą maksymalną wartość z 3 liczb. maximum_of(a, b, c).

def max_of_two(val1, val2):
    return val1 if val1 > val2 else val2

    # if val1 > val2:
    #     return val1
    # else:
    #     return val2


def maximum_of(a, b, c):
    tmp = max_of_two(a, b)
    return max_of_two(c, tmp)

def main():
    # ---- glowny kod
    x, y, z = [15, 15, 2]
    result = maximum_of(x, y, z)
    print(result)

main()