"""
dice rolling
"""

import random


print("Welcome to dice rolling simulator")
print("Get ready to roll!")
number=int(input("How many rolls should we simulate?: "))

one=print("One:")
two=print("Two:")
three=print("Three:")
four=print("Four:")
five=print("Five:")
six=print("Six:")

counter = 0


for attempt in range (1,6):
    x = random.random()
    if number == 1:
        print("#")
    elif number==2:
        print("#")
    elif number==3:
        print("#")
    elif number==4:
        print("#")
    elif number==5:
        print("#")
    elif number==6:
        print("#")


