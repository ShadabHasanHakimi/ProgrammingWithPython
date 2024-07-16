# Once a program terminates, the content it have will be lost, in order to persist the data forever, we use files
# A file is used for storage, a python program can read and write into files

# By default a file is opened in read mode
f = open("25_file.txt")
data = f.read()
print(data)
f.close()

# writing in a file
# this method will create a new file
st = "You can write into a file using this method!"
f = open("25_newfile.txt", "w")
data = f.write(st)
f.close()

f = open("25_newfile.txt")
data = f.read()
print(data)
f.close()