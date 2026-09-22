class Employee:
    company = "Google"
    salary = 100

anish = Employee()
rajni = Employee()
anish.salary = 300
rajni.salary = 400

print(anish.company)
print(rajni.company)
Employee.company = "YouTube"
print(anish.company)
print(rajni.company)
print(anish.salary)
print(rajni.salary)