w = input("Podaj wagę ->")
h = input("Podaj wzrost ->")

w = float(w.replace(",", "."))
h = float(h.replace(",", "."))

bmi = w / (h ** 2)
print("Your BMI is:", round(bmi, 2))
