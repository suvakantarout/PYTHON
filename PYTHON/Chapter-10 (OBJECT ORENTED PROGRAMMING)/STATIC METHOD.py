class Employee:
    company = "Google"

    def getsalary(self,signature):
        print(f"salary for this Employee working in {self.company} is {self.salary}\n{signature} ")

    @staticmethod
    def greet():
        print("Good Morning,Sir")
        print("Thanks!")
   
Ram = Employee()
Ram.salary = 100000
Ram.getsalary("CEO:Google")  #OR  Employee.getsalary(Ram)
Ram.greet()
