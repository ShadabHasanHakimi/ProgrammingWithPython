# it is collection of key-value pairs
marks = {
    "shadab": 100,
    "adab": 67,
    0: "namuna"
}

empty = {} #empty dictionary

print(marks, type(marks))

# How to access dictionary
print(marks["adab"]) # not like marks[0]
print(marks[0])

# properties of dictionaries
# 1. unordered
# 2. mutable
# 3. it is indexed
# 4. cannot contain duplicate keys

print(f"keys: {marks.keys()}")
print(f"items: {marks.items()}")

# existing keys will be updated whereas new keys will be added
marks.update({"shadab": 99, "pappu": 74})
print(marks)

