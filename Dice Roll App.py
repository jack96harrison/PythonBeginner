
"""
The point of this app is to resemble a dice roll.
It can roll 1 to 6.
The result must be random each time.
"""
import random

x = 0

while x == 0:

    print("Step Right Up And Roll Your Dice")

    dice_roll_options = [1, 2, 3, 4, 5, 6]

    print(random.choice(dice_roll_options))

    answer = input("Would you like another go? ")
    if answer == "yes" or answer == "y":
        x = 0

    else:
        x += 1

print("Thank you for playing")

