#Magician Game
secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

guess = int(input('Come on! Have a guess! '))
while guess != secret_number:
    guess = int(input('Come on! Have a guess! '))
print('Well done, Muggle. You are free now.')
