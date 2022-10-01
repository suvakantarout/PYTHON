# Ex:1
class Employee:
    company = "Google"
    salary = 30000

Ram = Employee()
Sam = Employee()

# Creating Instance Atributes  "salary" for both the objects
Ram.salary = 50000        
Sam.salary = 70000
print(Ram.salary)
print(Sam.salary)



Ex:2
class Employee:
    company = "Google"
    salary = 30000
    
Ram = Employee()
Sam = Employee()

# Remove the Instance Atributes:
print(Ram.salary)
print(Sam.salary)



Ex:3
class Employee:
    company = "Google"
    salary = 30000
    
Ram = Employee()
Sam = Employee()

Employee.salary = 20000         # Changing the class through "Class Atribute"
print(Ram.salary)
print(Sam.salary)

        # OR

class Employee:
    company = "Google"
    salary = 30000
    
Ram = Employee()
Sam = Employee()

Ram.salary = 10000      
print(Ram.salary)
print(Sam.salary)
 
