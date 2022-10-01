# string_slicing_and_Indexing:

# String indexing:
Greeting = "Good morning,"
name = "sunit :)"
print(Greeting + name)
# OR
c = Greeting + name    # concatnating two strings 
print(c)
name = "sunit"
print(name[0])         
print(name[3])       # When you want to print a single character of a word
print(name[4])

# String slicing:
name = "sunit"
print(name[0:3])
print(name[2:4])
print(name[:4])   #it same as name[0:4]
print(name[0:])
print(name[3:])


# slicing_with_skip_value:
name = "sunitisgood"
print(name[1:8:2])
print(name[0:6:4])
