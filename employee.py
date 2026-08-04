
class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def display(self):
        print("Employee Name:", self.name)
        print("Employee ID:", self.emp_id)

    def __init__(self, name, emp_id, department):
        super().__init__(name, emp_id)
        self.department = department

    def show_manager(self):
        self.display()
        print("Department:", self.department)

class Developer(Employee):
    def __init__(self, name, emp_id, language):
        super().__init__(name, emp_id)
        self.language = language

    def show_developer(self):
        self.display()
        print("Programming Language:", self.language)

m = Manager("Ravi", 101, "HR")
d = Developer("Kavyaa", 102, "Python")

print("Manager Details")
m.show_manager()

print("\nDeveloper Details")
d.show_developer()
