# Question 1
'''
Ans 1: d. set()

Ans 2: d) s={san} 

Ans 3: a. True 

Ans 4: b. t[3] = 45

Ans 5: d. (2,3)
'''


# Question 2
'''
Ans a: <class 'list'>

Ans b: [1, 2, 3, None, (), []]

Ans c: Sum= 6

And d: ('PYTHON',)
1
3
'''


# Question 3
'''
ListA= [1, 4, 3, 0] 
ListB= ['x', 'z', 't', 'q'] 
ListA.sort ( ) 
print(ListA )
ListA.insert (0, 100)
ListA.remove (3) 
ListA.append (7)
ListC=ListA+ListB
ListB.pop ( ) 
ListA.extend ( [4, 1, 6, 3] ) 

Ans 1: No error

Ans 2: No error

Ans 3: No error

Ans 4:[0, 1, 3, 4]

Ans 5:[0, 1, 3, 4]

Ans 6:[0, 1, 3, 4]

Ans 7:[0, 1, 3, 4]

Ans 8:[0, 1, 3, 4]

Ans 9:[0, 1, 3, 4]

Ans 10:[0, 1, 3, 4]
'''

# Question 4
'''
students = ["Arun", "Pawan", "Tausif", "Mahesh", "Shadab"]
# Ans 1:
print(students)
# Ans 2:
name = input("Enter a new name: ")
students.append(name)
# Ans 3:
print(students)
# Ans 4:
i = int(input("Enter a index: "))
if(i<len(students)):
    print(students[i])
else:
    print("Index provided is greater than the last index!")
# Ans 5: 
students =["Kamal"] + ["Sanjana"] + students[0:]
# Ans 6:
print(students)
# Ans 7: 
n = input("Enter a name: ")
if(n in students):
    students.remove(n)
else:
    students.append(n)
# Ans 8:
students_rev = students[-1::-1]
# Ans 9
print(f"Original list: {students_rev}, Reversed list: {students}")
# Ans 10
students.pop()
print(students)
'''


# Ans 5: {'c'}


# Ans 6:
'''
n = int(input("Enter the number of elements for each set: "))

T1 = set()
T2 = set()

print("Enter elements for the first set:")
for _ in range(n):
    T1.add(int(input()))
    
print("Enter elements for the second set:")
for _ in range(n):
    T2.add(int(input()))
    
merged_set = T1.union(T2)
sorted_list = sorted(merged_set)

print("T1 =", T1)
print("T2 =", T2)
print("T3 =", sorted_list)
'''


# Ans 7:
'''
A = {'a', 'b', 'd', 'e'}
B = {'b', 'c', 'e', 'f'}
C = {'d', 'e', 'f', 'g'}
# Ans i:
lhs1 = A.intersection(B.union(C))
rhs1 = (A.intersection(B)).union(A.intersection(C))
print(f"LHS: {lhs1}, RHS: {rhs1}")
print("Hence Proved!")

# Ans ii:
lhs2 = A.union(B.intersection(C))
rhs2 = (A.union(B)).intersection(A.union(C))
print(f"LHS: {lhs2}, RHS: {rhs2}")
print("Hence Proved!")
'''

# Ans 8:
'''
set1 = { 10, 20, 30, 40, 50 } 
set2 = { 30, 40, 50, 60, 70 } 

# Ans a:
print(f"Set of identical items is: {set1.intersection(set2)}")
# Ans b:
print(f"Set without duplicates: {set1.union(set2)}")
# Ans c:
print(f"Set of all elements in either A or B, but not both: {set1.symmetric_difference(set2)}")
# Ans d:
print(f"Common elements in set: {set1.intersection(set2)}")
'''