def isYearLeap(year):
    if year%4 != 0:
        leap = False
    elif year%100 != 0:
        leap = True
    elif year%400 != 0:
        leap = False
    else:
        leap = True
    return leap

def daysInMonth(year, month):
    leap = isYearLeap(year)
    days_per_month = [31, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if leap:
        days_per_month.insert(1, 29)
    else:
        days_per_month.insert(1, 28)
    return days_per_month[month-1]

testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 1, 11]
testResults = [28, 29, 31, 30]
for i in range(len(testYears)):
	yr = testYears[i]
	mo = testMonths[i]
	print(yr, mo, "->", end="")
	result = daysInMonth(yr, mo)
	if result == testResults[i]:
		print("OK")
	else:
		print("Failed")
