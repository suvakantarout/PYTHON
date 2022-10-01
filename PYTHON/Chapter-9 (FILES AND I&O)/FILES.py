# use open function to read the content of the file.
f = open('sample.txt', 'r')      # by defult the mode is r 
data = f.read()
print(data)
f.close()                         
