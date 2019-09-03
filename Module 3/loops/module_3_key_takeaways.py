print()
print('Exercise 2')
print()

for i in range(1,11):
    if not i%2:
        print(i)

print()
print('Exercise 2')
print()

x = 1
while x < 11:
    if x%2:
        print(x)
    x += 1

print()
print('Exercise 3')
print()

pre_at = ''
for ch in "peter.smith@bt.co.uk":
    if ch == "@":
        break
    pre_at += ch
print(pre_at)

print()
print('Exercise 4')
print()

new_string = ''
for digit in "08176730707650":
    if digit == "0":
        digit = "x"
    new_string += digit
print(new_string)
