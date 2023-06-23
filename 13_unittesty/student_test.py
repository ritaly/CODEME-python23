import unittest
from student import Student

class TestStudent(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print('~~~~setUpClass~~~~')

    def setUp(self) -> None:
        print('-------setUp---------')
        print()

    def test_email_change(self):
        print('TEST1')
        # given
        anna = Student('anna', 'snow', 4.6)
        expected_email = 'anna.snow@uam.com'
        self.assertEqual(anna.email, expected_email)
        # when akcja -> "kiedy anna zmieniła nazwisko"

        anna.last = 'summer'
        new_expected_email = 'anna.summer@uam.com'
        # then

        self.assertEqual(anna.email, new_expected_email)


    def test_fullname(self):
        print('TEST2')
        anna = Student('anna', 'snow', 4.6)
        self.assertEqual(anna.fullname, 'Anna Snow')


        anna.last = 'summer'
        expected_fullname = 'Anna Summer'

        self.assertEqual(anna.fullname, expected_fullname)



    def test_grant_scholarship(self):
        print('TEST3')
        anna = Student('anna', 'snow', 4.6)
        adam = Student('adam', 'kowalski', 3.5)

        self.assertIsNone(anna.scholarship)

        anna.grant_scholarship()
        self.assertTrue(anna.scholarship)

        adam.grant_scholarship()
        self.assertFalse(adam.scholarship)


    def tearDown(self) -> None:
        print('-------- tearDown ----------')
        print()

    @classmethod
    def tearDownClass(cls) -> None:
        print('~~~~~tearDownClass~~~~~~~')
