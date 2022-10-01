with open('sample.txt_3', 'w') as f:
    a = f.write("i am writting")       # in write mode('w')
with open('sample.txt_3', 'r') as f:
    a = f.read()                       # in read mode('r')
print(a)
