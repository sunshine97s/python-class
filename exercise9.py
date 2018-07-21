from random import *
print("Difficult Levels:")
print("[E]asy")
print("[M]edium")
print("[H]ard")
Level = input("Choose difficult level: ")
print(Level)
guess = 0
a = 0

if Level == 'E' or 'e':
    a = (randint(1,6))
    print("Choose a number from 1 to 6")
elif Level == 'M' or 'm':
    a = (randint(1,20))
    print("Choose a number from 1 to 20")
else:
    a = (randint(1,100))
    print("Choose a number from 1 to 100")
command = input("Predict the number: ")
guess = guess + 1
result = 'wrong'
while result == 'wrong':
    if int(command) > a:
        print("You guessed too high")
        command = input("Try again: ")
        guess = guess + 1
    elif int(command) < a:
        print("You guessed too low")
        command = input("Try again: ")
        guess = guess + 1
    else:
        print("You guessed the correct number")
        result = 'correct'
        print("You guess " + str(guess) + " times")

