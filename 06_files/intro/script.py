handler = open("pan_tadzio.txt")
print(handler.readline())
handler.close()

print('-----------------')

with open("pan_tadzio.txt") as fo:
    print(fo.readline())
    print(fo)
