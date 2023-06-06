class Student:
    school = 'UAM'
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def __str__(self):
        email = self.email()
        return f'imię: {self.firstname}; nazwisko: {self.lastname}, wiek: {self.age}, email: {email}'

    def email(self):
        return f'{self.lastname}.{self.firstname[0]}@{self.school.lower()}.pl'

    def sound(self, number):
        return f'go {self.school}!' * number

anna = Student('anna', 'nowak', 23)
adam = Student('adam', 'snow', 22)

print(adam)
#
# print(anna.email())
# print(adam.email())
#
# anna.lastname = 'kowal'
# print(anna.lastname)
# print(anna.email())
#
# print(anna.sound(2))
#
# print(type(6))
# print(type(anna))

