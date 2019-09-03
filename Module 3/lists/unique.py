myList = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

for i in range(len(myList)-1):
    if myList[i] in myList[:i]:
        del myList[i]

print("The list with unique elements only:")
print(myList)
