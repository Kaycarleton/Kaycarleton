""""

"""
from statistics import mean

user_input=input("Enter your phrase here: ")
two_letters=[word[0:2] for word in user_input.split()]


print(two_letters)

consonant_vowel=('da','no','si','ha','ba','bo','su','mo')
consonant_consonant=('th', 'br','sh','sp','bl','ch')
vowel=('at','of','ev','ec','an')

first_letters=user_input.lower()

if consonant_vowel in user_input:
    print(user_input + (two_letters + 'ay'))
elif consonant_consonant in user_input:
    print(user_input + (two_letters +'ay'))
elif vowel in user_input:
    print(user_input + (two_letters +'ay'))

print(user_input)

#2. 
number=(len(user_input))
avg=mean(number)
print(avg)

#3. Not sure how to do 3 