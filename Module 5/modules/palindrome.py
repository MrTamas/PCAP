

def half_length(strng):
    length = len(strng)
    if length % 1 > 0:
        hl = length / 2 + 1
    else:
        hl = length / 2
    return hl

def check_palindrome(strng):
    palindrome = True
    half_length = len(strng) // 2
    length = len(strng) - 1
    for i in range(half_length):
        if strng[i] != strng[length-i]:
            palindrome = False
    if strng == '':
        palindrome = False

    if palindrome:
        return 'It\'s a palindrome!'
    else:
        return 'Nope, try again!'

word = input('Please provide a word: ')
word = word.lower()
word = ("").join(word.split())

print(check_palindrome(word))
