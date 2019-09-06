dict = {"cat" : "chat", "dog" : "chien", "horse" : "cheval"}
words = ['cat', 'lion', 'horse']

for word in words:
    if word in dict:
        print(word, "->", dict[word])
    else:
        print(word, "is not in dictionary")
