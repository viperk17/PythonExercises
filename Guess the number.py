from random import randint
import sys

ans = randint(1,10)

while True:
    try:
        print(ans)
        guess = int(input("Guess a number in 1-10: "))
        if 0 < guess < 11:
            if guess == ans:
                print("You won")
                break
        else:
            print("Enter 1-10.")
    except ValueError:
        print("Please enter a number... ")
        continue