from student import Student
import datetime

anna = Student('nna', 'Kowalska', 23, 4.5)
jan = Student('Jan', 'Nowak', 21, 4.4)

print(anna.email)
anna.name = 'Anna'
print(anna)
print(anna.email)
print(anna.fullname)

anna.fullname = "Wisniewska Anna"
print(anna)

del anna.fullname

print(anna)


# anna.grand_scholarship()
# jan.grand_scholarship()
#
# Student.set_min_avg(4.3)
# anna.grand_scholarship()
# jan.grand_scholarship()
#
# print(anna.min_avg)
# print(jan.min_avg)

# today = datetime.datetime.today()
# print(today)
#
# epiphany = datetime.datetime.strptime('2023-01-06', '%Y-%m-%d')
#
# print("Are students today at University?", Student.is_academic_day(epiphany))
