digits = input("Please add your birthday in the format YYYYMMDD")



import time
while len(digits) > 1:
    sum = 0
    for d in digits:
        sum += int(d)
    digits = str(sum)

print(sum)
