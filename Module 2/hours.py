hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

start = str(hour) + ":" + str(mins) # put your code here
hours_passed = (mins + dura)//60
hour_end = (hour + hours_passed)%24
minutes_end = (mins + dura)%60
end = str(hour_end) + ":" + str(minutes_end)

print(end)
