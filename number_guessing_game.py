import random

number = random.randint(1, 10)

print("Guess a number between 1 and 10")

attempts = 0

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < number:
        print("Too low!")

    elif guess > number:
        print("Too high!")

    else:
        print("Correct!")
        print("You guessed in", attempts, "attempts")
        break

print("Game Over")
print("Thanks for playing!")
print("Practice Python daily!")