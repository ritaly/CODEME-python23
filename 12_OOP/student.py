import datetime


class Student:
    university = 'UAM'
    min_avg = 4.5

    def __init__(self, name, last, age, student_avg):
        self.name = name
        self.last = last
        self.age = age
        self.student_avg = student_avg

    def __str__(self):
        return self.name.capitalize() + " " + self.last.capitalize()

    def email(self):
        return f'{self.last.lower()}.{self.name[0].lower()}@university.com'

    def grand_scholarship(self):
        if self.student_avg >= self.min_avg:
            print('Przyznano stypendium')
        else:
            print('Odmowa przyznania stypendium')

    @classmethod
    def set_min_avg(cls, new_min_avg):
        cls.min_avg = new_min_avg

    @staticmethod
    def is_academic_day(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        else:
            return True


anna = Student('Anna', 'Kowalska', 23, 4.5)
jan = Student('Jan', 'Nowak', 21, 4.4)
# anna.grand_scholarship()
# jan.grand_scholarship()
#
# Student.set_min_avg(4.3)
# anna.grand_scholarship()
# jan.grand_scholarship()
#
# print(anna.min_avg)
# print(jan.min_avg)

today = datetime.datetime.today()
print(today)

print("Are students today at University?", Student.is_academic_day(today))
