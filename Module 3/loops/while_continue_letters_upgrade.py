# Prompt the user to enter a word
# and assign it to the userWord variable.
userWord = input('Give me a word! ')
userWord = userWord.upper()
wordWithoutVowels = ''
for letter in userWord:
    if letter in ['A', 'E', 'I', 'O', 'U']:
        continue
    wordWithoutVowels += letter
    # Complete the body of the for loop.
print(wordWithoutVowels)
