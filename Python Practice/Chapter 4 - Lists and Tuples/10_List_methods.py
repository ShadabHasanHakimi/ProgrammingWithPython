# string methods return new string and do not change the original string
# whereas list method make changes in original list

friends = ["apple", "orange", "rohan", 123, 22.22, False]

friends.append("Shadab")
print(friends)

l1 = [2, 12, 33, 7, 62, 31, 1, 22]
l1.sort()
print(l1)

l1.reverse()
print(l1)

# insert method will insert 3333 at 3 index
l1.insert(3, 3333)
print(l1)

print(l1.pop(3))