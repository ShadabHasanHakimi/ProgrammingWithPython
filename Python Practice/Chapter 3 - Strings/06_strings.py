a = 'Shadab'
b = "Shadab"
c = '''Shadab'''

print(c)

# Slicing in python
# String is immutable
print(a[0:4]) # print a upto 0-4(excluding 4)

print(a[-1]) # index starts from -1 from rhs

print(a[-4: -1])
print(a[2: 5]) # convert negative indexing into positive

# Slicing with skip value
print(a[1: 5: 2])

