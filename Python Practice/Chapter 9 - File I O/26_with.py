# With statement

with open("25_file.txt") as f:
    print(f.read())
# now you don't have to close the file explicitly, because 'with' closes the file automatically
