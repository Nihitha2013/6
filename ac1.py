import random
play=True
n=str(random.randint(1,10))

print("Let's guess number between 1 to 10")
print("Game will end when you guess correct number")

while play:
    guess=input("Enter guess number ")
    if n==guess:
        print("Correct guess")
        print("The number was",n)
        break
    else:
        print("Wrong guess, try again")