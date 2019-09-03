# Copying the whole list
list1 = [1]
list2 = list1[:]
list1[0] = 2
print(list2)

# Copying part of the list
myList = [10, 8, 6, 4, 2]
newList = myList[1:3]
print(newList)

# From the back
myList = [10, 8, 6, 4, 2]
newList1 = myList[1:-1]
print(newList1)

# Empty slice
newList2 = myList[-1:1]
print(newList2)

# Eliminating arguments
newList3 = myList[:3]
print(newList3)

newList4 = myList[3:]
print(newList4)

# using delete
del myList[1:3]
print(myList)

myList = [10, 8, 6, 4, 2]
del myList[:]
print(myList)

del myList
print(myList)
