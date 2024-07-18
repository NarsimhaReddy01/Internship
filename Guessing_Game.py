import random

def main():
    print("Welcome To The Number Guessing Game!")
    random_number = random.randint(1, 100)
    attempts = 0

    while True:
        guess = int(input("Guess a number between 1 and 100: "))
        attempts += 1

        if guess <random_number:
            print("Too low, try again.")
        
        elif guess > random_number:
            print("Too high, try again.")
        
        else:
            print(f"Congratulations, you guessed the correct number in {attempts} attempts.")
            break
if __name__ == "__main__":
    main()
