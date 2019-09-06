def get_message():
    prompt1 = 'Please add your message: '
    
    try:
        message = input(prompt1)
    except:
        print('Please enter a message made up of numbers and letters.')
    return message

def get_ran():
    prompt2 = 'Please choose a shift range between 1 and 25: '
    try:
        ran = int(input(prompt2))
        assert ran in range(1, 25)
    except:
        print("Please choose a positive whole number between 1 and 25.")
    return ran

def caesar_it():
    message = get_message()
    ran = get_ran()
    c_message = ''
    for i in message:
        if i.isalpha():
            code_point = ord(i) + ran
            if i.isupper() and code_point > 90 or i.islower() and code_point > 122:
                code_point -= 26
            j = chr(code_point)
        else:
            j = i
        c_message += j
    return c_message

print(caesar_it())
