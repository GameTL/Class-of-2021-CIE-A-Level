import random
print("Hello what's your age?")
number = input()
number = random.randint(1, 20)
print("I'm thinking of a whole number what is it, ma dude?")
#print(number)
guess = input()
guess = int(guess)

if guess != number:
    print('Nope')
if guess == number:
    print('Good')
