import unittest
from student import Student


class TestStudent(unittest.TestCase):

    def setUp(self):
        self.student_1 = Student('Ali', 'Muhammad', 'CS', 19, 'Male')

    def test_email(self):
        self.assertEqual(self.student_1.email(), 'AMuhammad@email.com')
        self.student_1.first = 'Hamza'
        self.assertEqual(self.student_1.email(), 'HMuhammad@email.com')

    def test_fullname(self):
        self.assertEqual(self.student_1.fullname(), 'Ali Muhammad')
        self.student_1.first = 'Hamza'
        self.assertEqual(self.student_1.fullname(), 'Hamza Muhammad')

    def test_major(self):
        self.assertEqual(self.student_1.get_major(), 'CS')

    def test_get_age(self):
        self.assertEqual(self.student_1.get_age(), 19)

    def test_get_gender(self):
        self.assertEqual(self.student_1.get_gender(), 'Male')


if __name__ == '__main__':
    unittest.main()
