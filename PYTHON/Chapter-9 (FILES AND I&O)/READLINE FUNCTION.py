f = open('sample.txt')
data = f.readline()                       # read first line of the sample.txt
print(data)
data = f.readline()                       # read second line of the sample.txt
print(data)
data = f.readline()                       # read third line of the sample.txt
print(data)
data = f.readline()                       # read fourth lineof the sample.txt......and so on.....
print(data)
f.close()
