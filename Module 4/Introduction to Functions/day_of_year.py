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

def dayOfYear(year, month, day):
    if year < 1528 or month < 1 or month > 12 or day < 1 or day > daysInMonth(year, month):
        day_of_year = None
    else:
        days_up_to_last_month = 0
        for i in range(1,month):
            days_up_to_last_month += daysInMonth(year, i)
        day_of_year = days_up_to_last_month + day
    return day_of_year

