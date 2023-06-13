class Point:
    def __init__(self, num):
        self.__x = '0'
        self.num = num

    def get_x(self):
        return self.__x

    def set_x(self, x):
        # tutaj jakies sprawdzenie czy wolno mi ustawić zmianę
        self.__x = x


point = Point(2)
print(point.__x)
point.set_x(2)
print(point.get_x())
