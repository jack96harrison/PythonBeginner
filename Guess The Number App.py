"""
The app generates a random number -done
Asks the user to guess the number
Informs the user if the guess is right or wrong and if the guess was too high or too low
If the user guesses right then they get a congratulation message
A function is needed to verify the input is a number
"""
import random

x = 0

number = range(1, 11)

num = random.choice(number)

while x == 0:

    user_input = input("Please guess a number between 1 and 10: ")
    user_input = int(user_input)

    if 1 <= user_input <= 10:

        if user_input == num:
            print("CONGRATULATIONS! YOU GUESSED CORRECT")
            x += 1
        elif user_input > num:
            print("SORRY YOU GUESSED TOO HIGH, GUESS AGAIN!")
        elif user_input < num:
            print("SORRY YOU GUESSED TOO LOW, GUESS AGAIN!")
        else:
            print("Oops Something Went Wrong!")

    else:
        print("PLEASE ENTER A VALID NUMBER BETWEEN 1 and 10")

        
