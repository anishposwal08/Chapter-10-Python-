class Employee:
    company = "Google"
    salary = 100

anish = Employee()
rajni = Employee()

# Creating instance attribute salary for both the objects
# anish.salary = 300
# rajni.salary = 400
anish.salary = 45
print(anish.salary)
print(rajni.salary)

# Below line throws an error as address is not present in instance/class 
# print(rajni.address) 