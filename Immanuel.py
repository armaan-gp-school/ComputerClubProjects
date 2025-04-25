import random

print("Welcome to the 3-digit number guessing game! (made by Immanuel)")
print("You have to guess a 3-digit number from the digits 0 to 5.")
print("After each guess, I will tell you how many digits are correct.")
print("Let's start!")

# Generate a random 3-digit number
secret_number = ''.join(random.choice('012345') for _ in range(3))

guess = input("Enter your guess (3 digits): ")
while True:
    if (len(guess) != 3) or (not guess.isdigit()) or (int(guess) < 0) or (int(guess) > 555):
        print("Invalid input. Please enter a 3-digit number from the digits 0 to 5.")
        guess = input("Enter your guess (3 digits): ")
        continue

    correct_digits = 0
    for a, b in zip(guess, secret_number):
        if a == b:
            correct_digits += 1

    if correct_digits == 3:
        print(f"Congratulations! You've guessed the correct number: {secret_number}")
        break
    else:
        print(f"You have {correct_digits} correct digits.")
        guess = input("Try again (3 digits): ")