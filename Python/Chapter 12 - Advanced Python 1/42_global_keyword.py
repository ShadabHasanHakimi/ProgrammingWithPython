a = 89

def fun():
    # if global a is not there then a printed will be the a of function
    global a
    # a = 3
    print(a)
    
fun()
print(a)