class Employee:
    company = "Google"

Ram = Employee()                       # Class Atributes for both the objects
Sam = Employee()
print(Ram.company)
print(Sam.company)

Employee.company = "YouTube"           # Here in (Class Atributes) i will change the class name by taking the "class"             
print(Ram.company)
print(Sam.company)


