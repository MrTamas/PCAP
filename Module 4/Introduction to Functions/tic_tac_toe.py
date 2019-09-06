# some issues: empty or non-integer entries cause errors

from random import randrange

def DisplayBoard(board):
    divider_section1 = '+' + 7*'-'
    divider1 =  3 * divider_section1 + '+'
    divider_section2 = '|' + 7*' '
    divider2 =  3 * divider_section2 + '|'
    s = 3 *' '
    divider3 = s + '|' + s

    for i in range(3):
        print(divider1)
        print(divider2)
        data_row = '|' + s + board[i][0] + divider3 + board[i][1] + divider3 + board[i][2] + s + '|'
        print(data_row)
        print(divider2)
    print(divider1)


def MakeListOfFreeFields(board):
    empty_fields = []
    for i in range(3):
        for j in range(3):
            cell = board[i][j]
            if cell != 'X' and cell != 'Ø':
                empty_fields.append((i, j))
    return empty_fields

def EnterMove(board):
    print('Your move!')
    empty = False
    while not empty:
        try:
            next_move = int(input('Row: ')) - 1, int(input('Column:')) - 1
        except ValueError:
            print('Numbers between 1 and 3, please!')
            continue
        i = next_move[0]
        j = next_move[1]
        empty = next_move in MakeListOfFreeFields(board)
        if empty and i < 3 and i >=0 and j < 3 and j >= 0:
            board[i][j] = 'Ø'
        else:
            print('Numbers between 1 and 3, please, and no replacing!')
    return board

def VictoryFor(board, sign):
    win = False
    for i in range(3):
        if board[i][0] == board[i][1] and board[i][0] == board[i][2] and board[i][0] == sign:
            win = True
    for i in range(3):
        if board[0][i] == board[1][i] and board[0][i] == board[2][i] and board[0][i] == sign:
            win = True
    if board[0][0] == board[1][1] and board[0][0] == board[2][2] and board[0][0] == sign:
        win = True
    if board[0][2] == board[1][1] and board[0][2] == board[2][0] and board[0][2] == sign:
        win = True
    return win

def DrawMove(board):
    print('Computer\'s move')
    empty = MakeListOfFreeFields(board)
    next_move_pick = randrange(len(empty))
    next_move = empty[next_move_pick]
    i = next_move[0]
    j = next_move[1]
    board[i][j] = 'X'
    return board
    
def play():
    board = [[str(x+y) for x in range(1,4)] for y in range(0, 10, 3)]
    board[1][1] = "X"

    DisplayBoard(board)

    empty = MakeListOfFreeFields(board)
    while len(empty) > 0:
        board = EnterMove(board)
        DisplayBoard(board)
        if VictoryFor(board, "Ø"):
            print('You won! Congrats!')
            break
        board = DrawMove(board)
        DisplayBoard(board)
        if VictoryFor(board, "X"):
            print('Good effort! Perhaps next time.')
            break
        empty=MakeListOfFreeFields(board)
    else:
        print('It\'s a draw!')

