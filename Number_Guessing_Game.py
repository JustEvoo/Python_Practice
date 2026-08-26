import random
low = 1
high = 100
answer = random.randint(low, high)
guesses = 0
is_running = True
print("Welcome to the Number Guessing Game")
#Game
while is_running:
    guess = input("Guess a number: ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        if guess < low or guess > high:
            print(f"Please enter a number between {low} and {high}")

        if guess == answer:
            print("Congratulations! You guessed the number!")
            is_running = False
        else:
            print("Sorry, you lost the number!")

print("Thanks for playing!")





