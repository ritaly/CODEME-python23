class Account:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.__number = '12 3000 0000 1212 2111'

    def show_number(self):
        print('Account number:', self.__number)

    def modify_number(self, new_number):
        # tutaj jakies sprawdzenie czy wolno mi ustawić zmianę
        self._number = new_number

user = Account('Anna', 'Kowal')
print(user.firstname)
print(user.lastname)
user.show_number()
user.__number = '1234'
user.show_number()
user.modify_number('12 1234 1234 1234 1234')
user.show_number()