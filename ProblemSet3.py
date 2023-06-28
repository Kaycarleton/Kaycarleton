"""
Interest Minigame
"""

print ("We are currently offering an amazing 1.5% on 5 year CDs")
print ("Tell me how much you got...")
print ("...I'll tell what it will be over the next 5 years.")

i = float (input("Enter your initial deposit: "))

x = 1

while x < 6:
    round(i, 2)
    print ("Year " + str(x) + " = " + str(round(i, 2)))
    x=x+1
    i = i*1.015