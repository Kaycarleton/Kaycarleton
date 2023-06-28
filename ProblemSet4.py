"""
Reaction Time
"""

print("When prompted hit the Enter key")

import time
from time import sleep
import random

random_number= random.randint(0,5)
sleep_time=sleep(random_number)
start=time.time()

enter=input("Quick hit the Enter Key")
end=time.time()



print("that was fast. It only took you {:,.3}".format(end-start), "seconds to hit Enter")




