# functions:

# Ex:
def mysum(num1, num2):
    return num1 + num2
s = mysum(17,25)
print(s)

# Quick Quiz:
def greet(name):
    print("Good Day," + name)
greet("Sunit")



# Funcions with Arrangements :

# Ex-1
def greet(name):
    print("Good Day," + name)

#Ex-1
def mysum(num1, num2):
    return num1 + num2

greet("Sunit")
s = mysum(5, 55)
print(s)


# Ex-2
def greet(name):
    greet = "Hello " + name
    return greet                           # Here (return greet) means the value of 'greet' returns and the value of 'greet' is asign to 'a'
a = greet("harry")
print(a)