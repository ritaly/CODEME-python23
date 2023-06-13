# zwierze

# ssak <- zwierze

# pies <-ssak
# kot <- ssak
# czlowiek <- ssak


class Animals:
    def __init__(self):
        print('Jesetem zwierzakiem')

class Mammals(Animals):
    def __init__(self):
        super().__init__()
        print('Jestem ssakiem')

class Fish(Animals):
    def __init__(self, name):
        self.name = name
        print('--FISH--')
        super().__init__()
        print('Jestem rybą ', name)
class Cat(Mammals):
    def __init__(self, name):
        self.name = name
        print('---CAT---')
        super().__init__()
        print('Jestem kotem ', name)

class Dog(Mammals):
    def __init__(self, name):
        self.name = name
        print('---DOG---')
        super().__init__()
        print('Jestem psem ', name)

class Man(Mammals):
    def __init__(self, name):
        self.name = name
        print('---MAN---')
        super().__init__()
        print('Jestem człowiekiem ', name)

cat = Cat('Filemon')
dog = Dog('Kapsel')
human = Man('Janusz')
fish = Fish('Nemo')