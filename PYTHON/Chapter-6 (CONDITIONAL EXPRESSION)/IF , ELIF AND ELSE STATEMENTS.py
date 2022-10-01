# "If" "Elif" "Else" Ladder in python:

# If statement:
a = 50
if(a>33):
    print("The value of a is grater than 33 ")                # Here the "if" function is true at first so, it prints "if"
elif(a>24): 
    print("The value of a is grater than 24")
elif(a<45):   
    print("The value of a is less than 45")
else:
    print("the value of a is not grater than 24 and not less than 45 ")


# Elif statement:
if(a>55):
    print("The value of a is grater than 55 ")
elif(a>24): 
    print("The value of a is grater than 24")                   # Here the "elif" function is true at first so, it prints "elif"
elif(a<45):   
    print("The value of a is less than 45")
else:
    print("the value of a is not grater than 24 and not less than 45 ")     # Here all functions are false so, it ptints "else"


# Else statement:
if(a>55):
    print("The value of a is grater than 55 ")
elif(a>65): 
    print("The value of a is grater than 65")
elif(a<30):   
    print("The value of a is less than 30")
else:
    print("the value of a is not grater than 24 and not less than 45 ")     # Here all functions are false so, it ptints "else"



# Multiple if statements:
if(a>55):
    print("The value of a is grater than 55 ")
if(a>65): 
    print("The value of a is grater than 65")
if(a<75):   
    print("The value of a is less than 75 ")
if(a>80):
    print("The value of a is grater than 80")
else:
    print("the value of a is not grater than 24 and not less than 45 ")


# Ex:
a = 22 
if(a>9):
    print("Grater")                # This will print cause (a>9) its true
else:
    print("lesser")


# Quick Quiz:
age = int(input("Enter your age: "))
if age>=18:  
    print("yes")
else:    
    print("no")