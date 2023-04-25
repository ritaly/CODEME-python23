fahr = 0

while fahr <= 200:
    celc = round(5 / 9 * (fahr - 32), 2)
    print(f"temp {fahr} F -> {celc} C")
    fahr += 20