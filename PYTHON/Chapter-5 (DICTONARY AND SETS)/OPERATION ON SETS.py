# Operation_on_sets:

s = {1,8,2,3}
print(s)

# len operation:
len(s)
print(len(s))

# remove operation:
s.remove(8)
print(s)

# pop operation:
s = {1,8,2,3}
s.pop()
print(s)                         # it will remove any element from the set

# clear operation:
s.clear()
print(s)                         # it will make the set empty

# union opeartion:
s.union({8,11})
print(s)

# intersection operation:
s.intersection({8,11})
print(s)