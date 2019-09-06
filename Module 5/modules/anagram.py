def check_anagrams():
    my_words = [input('Please add a word: '), input('And another: ')]

    anagrams = True

    for i in range(len(my_words)):
        my_words[i] = my_words[i].lower()

    for l in my_words[0]:

        if l in my_words[1]:

            if my_words[0].count(l) != my_words[1].count(l):
                anagrams = False
        else:
            anagrams = False
    if my_words[0] == '':
        anagrams = False
    if anagrams:
        return "Yes, they are!"
    else:
        return "They\'re sadly not."

print(check_anagrams())
