class Employee:
    company = "Google"

    def getsalary(self):
        print(f"salary for this Employee working in {self.company} is {self.salary} ")

    def greet(self):
        print("Good Morning, Sir")

Ram = Employee()
Ram.salary = 100000
Ram.getsalary()  #OR  Employee.getsalary(Ram)
Ram.greet()

