from module import myFunc

# if a file is run from it's own file then __name__ will print __main__
# otherwise if the file is run in other file then it will print the name of the file
# in this file __name__ will print __main__ but in the module.py file, the __main__ in myFunc() will print 'module' 
print(__name__)