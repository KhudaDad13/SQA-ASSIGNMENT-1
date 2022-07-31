class Student:
    def __init__(self, first, last, degree, age, gender):
        self.first = first
        self.last = last
        self.degree = degree
        self.age = age
        self.gender = gender

    def email(self):
        return '{}{}@email.com'.format(self.first[0], self.last)

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def get_major(self):
        return self.degree

    def get_age(self):
        return self.age

    def get_gender(self):
        return self.gender


