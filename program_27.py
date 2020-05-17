class Student:
    def __init__ (self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation

    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False

student1 = Student("Jim", "Business", 3.15, False)
print(student1)
print(student1.on_honor_roll())
