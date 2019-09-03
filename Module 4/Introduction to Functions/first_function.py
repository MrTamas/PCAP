import time
from random import random

def type_out(message):
    for i in message:
        print(i, end='')
        time.sleep(random()*0.1)
    print()
def message():
    m1 = 'I have something to say.'
    m2 = 'It might be of use to you.'
    m3 = 'It is important.'
    m4 = 'Are you ready?'
    messages = [m1, m2, m3, m4]
    for m in messages:
        type_out(m)
        time.sleep(3 + random()*2)
