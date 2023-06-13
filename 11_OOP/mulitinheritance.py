class UsefulStuff:
    def __init__(self, name):
        print(name, 'is used to make life easier!')

class Watch():
    def __init__(self, name):
        print(name, 'is small and mesures time!')

class Phone():
    def __init__(self, name):
        print(name, 'makes a call!')

    def make_call(self):
        print('ring~ring')

class SmartWatch(Watch, Phone):
    def __init__(self):
        print('Smartwatch is great!')
        super().__init__('My smartwatch')

# thing = UsefulStuff('thing')
# watch = Watch('watch')
# phone = Phone('phone')
sw = SmartWatch()