# Create class Fox with attributes paws, ears, tail
# should include at least 1 method
class Canis:
    paws = 4
    ears = 2
    tail = 1

    def __init__(self):
        print("Jestem wilkowaty")

    def show_description(self):
        print('''Species of this genus are distinguished
                   by their moderate to large size, their massive,
                   well-developed skulls and dentition,
                   long legs, and comparatively short ears and tails''')


class Fox(Canis):  # lisy dziedziczą z wilkowatych
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "Lis istnieje!"

    def make_sound(self, sound):
        print("Lis:", sound * 2)

    def show_description(self):
        print('~~~ Wolfs ~~~')
        super().show_description()
        print('~~~ Foxes ~~~')
        print('''Foxes are small to medium-sized, 
        omnivorous mammals''')


lisek = Fox('Foxik')
lisek.show_description()