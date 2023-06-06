class Dog:
    def __init__(self, name, color, race):
        self.name = name
        self.color = color
        self.race = race

    def how(self, special_sound):
        return f'{special_sound}!!! - No {self.name} nie szczekaj ty {self.color} łobuzie!'


    def machaj(self):
        return f'sie macha {self.name}!' * 3




fafik = Dog('Fafik', 'czarny', 'buldog')
dyzio = Dog('dyzio', 'biszkoptowy', 'kundelek')

print(fafik.machaj())
print(dyzio.how('HAU'))