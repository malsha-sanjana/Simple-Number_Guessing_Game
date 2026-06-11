import random

attempts=0
secret_number=random.randint(0,100)

print("Welcome to Number Guessing Game!")
name=str(input("Enter your name: "))
print("Guess a number between 0 and 100.")

while True:

    while True:
        guess_number=str(input("Enter your guess number: "))
        try:
            guess_number=int(guess_number)
            attempts += 1
            break
        except:
            print("Invalid Number. Please Try Again.")

    if (guess_number>secret_number):
        print("Too High")

    elif(guess_number<secret_number):
        print("Too Low")

    else:
        print(name,",","you are correct!",",","You guessed it in",attempts,"attempts.")        
        break

