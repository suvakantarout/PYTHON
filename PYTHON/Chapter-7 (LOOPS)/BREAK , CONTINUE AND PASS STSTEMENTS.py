# Break statement :
for i in range(10):
    print(i)
    if i == 5:
        break                          # Itreturns (1,2,3,4,5)
else: 
    print("This is inside else of for")



# Continue statement :
for i in range(10):
    if i == 5:
        continue
    print(i)                      # here it will skip the number present in 'if' condition



# Pass statement :
l = [1,7,8]
for i in range(10):
    pass                          # it will do nothig 
                                  # without Pass python will throw error