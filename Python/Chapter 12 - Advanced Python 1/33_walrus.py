# using walrus (:=) operator
# using walrus operator we can do more than one operations is one if statement
# For eg: In below if statement, it means that if len of the given list is <= 3, then n = list and print the statement
if (n := len([1,2,3,4,5]))>3:
    print(f"List is too long ({n} elements, expected <= 3)") 
    
    
# before  
# values = [1, 2, 3, 4, 5]
# squares = []
# for val in values:
#     sq = val ** 2
#     if sq > 10:
#         squares.append(sq)
# print(sq)
    
    
# after
values = [1, 2, 3, 4, 5]
squares = [sq for val in values if (sq := val ** 2) > 10]
print(sq)
