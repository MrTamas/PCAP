c0 = int(input('Which number would you like to check? '))
counter = 0
while c0 !=1:
    if not c0%2:
        c0 /= 2
    else:
        c0 = 3*c0 + 1
    counter += 1
    print(counter, int(c0))
else:
    print('You\'ve reached one in', counter, 'steps.')
