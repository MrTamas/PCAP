# check sudoku
lines = ['295743861',
'431865927',
'876192543',
'387459216',
'612387495',
'549216738',
'763524189',
'928671354',
'154938672'
]


lines2 = ['195743862', '431865927', '876192543', '387459216', '612387495', '549216738', '763524189', '928671354', '254938671']

#for i in range(9):
#    lines.append(input('Please add a line: '))

# check function
def check_if_one(nset):
    single = True
    for i in range(1,10):
        if nset.count(str(i)) != 1:
            single = False
    return single

# check rows
def check_rows(table):
    single = True
    for i in range(9):
        print(table[i])
        if not check_if_one(table[i]):
            single = False
    return single

def check_columns(table):
    single = True
    for i in range(9):
        row = []
        for j in range(9):
            row += table[j][i]
        print(row)
        if not check_if_one(row):
            single = False
    return single

def check_squares(table):
    single = True
    counter = 0
    for i in range(0,8,3):
        for j in range(0,8,3):
            square = []
            for k in range(3):
                for l in range(3):
                    square += table[j+l][i+k]
                    counter += 1
            print(square)
            if not check_if_one(square):
                single = False
    return single

def check_sudoku(table):
    
    if check_rows(table) and check_columns(table) and check_squares(table):
        return "It\'s all good!"
    else:
        return "Nope, not yet..."
    
print(check_sudoku(lines))
