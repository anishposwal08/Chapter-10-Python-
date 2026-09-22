class Employee:
    company = "Google"
    def getSalary(self):
        print(f"Salary for this employee working in {self.company} is {self.salary}")

anish = Employee()
anish.salary = 100000
anish.getSalary() # Employee.getSalary(harry)