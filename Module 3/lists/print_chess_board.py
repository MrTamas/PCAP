def print_board():
    for j in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']:
        print
        print(j, end='')
        for i in range(8):
            print('|_', end="")
        print('|')
