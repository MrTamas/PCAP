word1 = input('Please add a word to search: ').lower()
word2 = input('Please add a supposed container word: ').lower()

container = True

for l in word1:
    pos = 0
    pos = word2.find(l, pos)
    if pos == -1:
        container = False
        break

print(container)
