class Employee:
    company = "Google"

Ram = Employee()
Sam = Employee()
print(Ram.company)
print(Sam.company)

# Instance Atributes "salary" for both the objects
Ram.salary = 50000     
Sam.salary = 70000
print(Ram.salary)
print(Sam.salary)


