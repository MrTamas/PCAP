myList = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
toFind = int(input('Find number: '))
found = False

for i in range(len(myList)):
    found = myList[i] == toFind
    if found:
        break

for numbers in myList:
    

print("The list with unique elements only:")
print(myList)
