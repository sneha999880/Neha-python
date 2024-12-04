class Person:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Name:", self.name)


class Staff(Person):
    def __init__(self, name):
        Person.__init__(self, name)


    def display(self):
        Person.display(self)

class TemporaryStaff(Staff):
    def __init__(self, name, days, hours_worked):
        Staff.__init__(self, name)
        self.days = days
        self.hours_worked = hours_worked

    def salary(self):
        total_salary = self.hours_worked * 150
        return total_salary

    def display(self):
        Staff.display(self)
        print("Number of Days:", self.days)
        print("Hours Worked:", self.hours_worked)
        print("Total Salary Earned:", self.salary())



temp_staff = TemporaryStaff("Ishika", 10, 8)
temp_staff.display()
