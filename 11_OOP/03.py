class Pen:
    def __init__(self, width):
        self.width = width

    def show_description(self):
        print('Pen')

    def set_width(self, width):
        self.width

class Pinaple:
    def __init__(self, color):
        self.color = color

    def show_description(self):
        print('Pinaple')

    def set_color(self, color):
        self.color = color


class PenPinapple(Pen, Pinaple):
    def __init__(self, color, width):
        super().set_width(width)
        super().set_color(color)

    def __str__(self):
        return f'Color: {self.color}, width: {self.width}'

    def show_description(self):
        super().show_description()


sth = PenPinapple('red', 345)
sth.show_description()
print(sth)

