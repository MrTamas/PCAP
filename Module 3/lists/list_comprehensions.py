squares = [x**2 for x in range(10)]
print(squares)

exp = [2**i for i in range(8)]
print(exp)

odds = [x for x in squares if x % 2 != 0 ]
print(odds)

#nested
board = [[[i+1,j+1] for i in range(8)] for j in range(8)]
