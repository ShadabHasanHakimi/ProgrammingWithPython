for i in range(100):
    if(i==34):
        break # Exit the loop
    print(i)
    
for i in range(10):
    if(i == 7 or i == 3):
        continue # skip this iteration (7 and 3 will not be printed). Only code below the continue will not be executed
    print(i)
    
for i in range(10):
    pass # it will not run the for loop and code after the for loop will be executed without an error