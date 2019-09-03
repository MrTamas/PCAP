rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)]

# book room in the 2nd building, 9th floor, room nr 13.
rooms[1][9][13] = True

# book more rooms

for i in [1, 5, 6, 7, 16]:
    rooms[2][14][i] = True

# release room in 1st building, 5th floor, room 1
rooms[0][4][1] = False

vacancies = 0

for roomNumber in range(20):
    if not rooms[2][14][roomNumber]:
        vacancies += 1

print(vacancies)
