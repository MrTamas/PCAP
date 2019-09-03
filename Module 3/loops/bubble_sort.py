# Bubble sort

list = [8,10,6,2,4]

for i in range(len(list)-1):
    for i in range(len(list)-1):
        if list[i] > list[i+1]:
            list[i], list[i+1] = list[i+1], list[i]

    print(list)
        
