# Dictonary_methods:

myDict = {
    "name" : "Suvakanta Rout",
    "age" : [17],
    "studies" : "CV Raman Global University",
    "branch" : "CSE(AL&ML)"
}

print(myDict["name"])
print(myDict["age"])
print(myDict["studies"])
print(myDict["branch"])

# Items method: 
myDict.items() 
print(myDict.items())          # print the("keys","values")of all contents of the dictonary

# keys method:
myDict.keys()
print(myDict.keys())              # in this way you can print  all "keys of a dictonary
print(list(myDict.keys()))        # in this way you can print all "keys" of a dictonary in a list

# Vlues method:
myDict.values()
print(myDict.values())           # in this way you can print the values of a dictonary
print(list(myDict.values()))     # in this way you can print all "values" of a dictonary in a list

# Update method:
updateDict = {
    "pssout from" : "Stewart Higher Secondary School",
    "stream" : "science"
}
myDict.update(updateDict)        # you can upadte dictonary by adding the ("key""values") pair in the upadteDict
print(myDict)

#  get method:
print(myDict.get("name"))
print(myDict["name"])            # This method is not applicable all time


# Difference between .get & [] syntex in the dictonary ?
print(myDict.get("name2"))       # returns none as name2 is not present in the dictonary
#print(myDict["name2"])           # Throws error as name2 is not present in the dictonary
