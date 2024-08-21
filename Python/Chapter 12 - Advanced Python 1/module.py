def myFunc():
    print("Hello world!")
myFunc()
    
print(__name__)
# if file is directly executed from its source file then execute if block
if __name__ == "__main__":
    print("We are directly running this code!")