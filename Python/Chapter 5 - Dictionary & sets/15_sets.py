# s = {1, 5, 32, "shadab", 7.3, True} : there can be multiple datatypes stored in a set 

empty = set() #empty set, don't use empty = {}, it will create empty dict

s = {1, 4, 23, 4, 4, 4, 12}
print(s) # elements cannot be repeated in a set

# set methods
s.add(19) #adds an element in the set
print(s)

# properties of sets
# 1. can store multiple datatypes
# 2. cannot contain duplicate values
# 3. unindexed
# 4. unordered

# len() function gives the length of the set
print(len(s))

# s.pop() removes 'random' element from the set