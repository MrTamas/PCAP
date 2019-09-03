for i in range(99,102):
    print(i, end=' ')
    gap_length = 6 - len(str(i))
    result = 2**i
    print(gap_length*' ', result)
