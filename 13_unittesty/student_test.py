import unittest
from student import Student

class TestStudent(unittest.TestCase):
    def test_email_change(self):
        # given
        anna = Student('anna', 'snow', 4.6)
        expected_email = 'anna.snow@uam.com'
        self.assertEqual(anna.email, expected_email)
        # when "kiedy anna zmieniła nazwisko"
        anna.last = 'summer'
        new_expected_email = 'anna.summer@uam.com'
        # then
        self.assertEqual(anna.email, new_expected_email)






