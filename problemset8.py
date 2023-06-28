"""
Random Integer Simulator
"""
import matplotlib.pyplot as plt
import random
import os

data=[random.randint(1,500) for x in range (1,500)]
for x in range (1,5):
    y=random.randint(1,2)
    z=random.randint(1,5)
    print(y)
    print(z)
print(data)

plt.plot(data)
plt.show()

print(os.getcwd())
print(os.listdir())

file=open('problemset8.py')
reading=file.readlines()

print(file)
