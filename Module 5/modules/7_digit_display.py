h = "#"
s = " "

line_type1 = [h, s, s]
line_type2 = [s, s, h]
line_type3 = [h, s, h]
line_type4 = [h, h, h]

def zero():
    return [line_type4, line_type3, line_type3, line_type3, line_type4]

def one():
    return [line_type2 for i in range(5)]

def two():
    return [line_type4, line_type2, line_type4, line_type1, line_type4]

def three():
    return [line_type4, line_type2, line_type4, line_type2, line_type4]

def four():
    return [line_type3, line_type3, line_type4, line_type2, line_type2]

def five():
    return [line_type4, line_type1, line_type4, line_type2, line_type4]

def six():
    return [line_type4, line_type1, line_type4, line_type3, line_type4]

def seven():
    return [line_type4, line_type2, line_type2, line_type2, line_type2]

def eight():
    return [line_type4, line_type3, line_type4, line_type3, line_type4]

def nine():
    return [line_type4, line_type3, line_type4, line_type2, line_type4]

functions = [zero(), one(), two(), three(), four(), five(), six(), seven(), eight(), nine()]


def display():
    digits = input("Numbers to display: ")
    line1 = []
    line2 = []
    line3 = []
    line4 = []
    line5 = []
    lines = [line1, line2, line3, line4, line5]
    for d in digits:
        n = int(d)
        f = functions[n]
        for i in range(len(lines)):
            lines[i].append(("").join(f[i]))
    print(3*" " + 3*len(line1)*"-" + (len(line1)-1)*4*"-")
    for line in lines:
        print("|  " + (" || ").join(line) + "  |")
    print(3*" " + 3*len(line1)*"-" + (len(line1)-1)*4*"-")

# digit = five()

# for i in range(len(digit)):
#    print((" ").join(digit[i]))

display()
