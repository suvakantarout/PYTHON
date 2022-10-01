# sets:

# An empty set can be created using below syntax :
s = set()
print(type(s))

s.add(4)
s.add(4)
s.add(4)
s.add(5)
s.add(5)
print(s)
s.add((2,3,5,6))               # you cannot add a lists in aset but you can add tuples in a set
                               # because sets are  not changable (list is changable but tuple is not changable )
print(s)
#a.add({"name" : "sunit"})        # you cannot add a dictonary to sets
#print(a)