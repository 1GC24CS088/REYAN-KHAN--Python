import random

number = random.randint(1, 50)
attempts = 0

print("Guess the number between 1 and 50")

while attempts < 5:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess == number:
        print("Congratulations! Correct answer.")
        print("Attempts:", attempts)
        break

    elif guess < number:
        print("Your guess is too low.")

    else:
        print("Your guess is too high.")

else:
    print("Game Over!")
    print("The correct number was:", number)