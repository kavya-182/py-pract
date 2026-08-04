# Parent Class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


# Derived Class: Student
class Student(Person):
    def __init__(self, name, age, roll_no):
        super().__init__(name, age)
        self.roll_no = roll_no

    def display_student(self):
        self.display()
        print("Roll Number:", self.roll_no)


# Derived Class: Teacher
class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def display_teacher(self):
        self.display()
        print("Subject:", self.subject)


# Main Program
s = Student("Kavyaa", 20, 101)
t = Teacher("Ravi", 40, "Python")

print("Student Details")
s.display_student()

print("\nTeacher Details")
t.display_teacher()