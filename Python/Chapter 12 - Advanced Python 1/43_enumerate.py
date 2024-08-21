l = [31, 12, 22, 78, 129, 1, 22]

# index = 0
# for item in l:
    # print(f"Item {index} in list is {item}.")
#     index+=1

# for doing the above task more easily, we use enumerate
for index, item in enumerate(l):
    print(f"Item {index} in list is {item}.")
    