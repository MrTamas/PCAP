variable1 = 2
variable2 = 1
print(variable1, variable2)
variable1, variable2 = variable2, variable1
print(variable1, variable2)


myList = [10, 1, 8, 3, 5]
length = len(myList)

for i in range(length // 2):
    myList[i], myList[length - i - 1] = myList[length - i - 1], myList[i]

print(myList)
