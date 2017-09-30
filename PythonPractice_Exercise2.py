"""
Ask the user to enter a number
If the answer is even then tell them it is even
If the answer is odd then tell them it is odd
"""

number = int(input("Please enter a number: "))

if number % 2 == 0 :
    print("You entered an even number")
else:
    print("You entered an odd number")

#
# # Extras:
# # If number is a multiple of 4 print something different
#
number = int(input("Please enter a number: "))

if number % 4 == 0 :
    print("You entered an even number which is divisible by 4")
elif number % 2 == 0:
    print("You entered an even number")
else:
    print("You entered an odd number")


# Ask use for 2 numbers num and divide
# If num divided by divide equals and even number then tell the user it is even
# Otherwise tell the user it is odd

num = (int(input("Please enter a number: ")))
divide = (int(input("Please enter a number to divide by: ")))

if num % divide == 0:
    print("The result is even")
else:
    print("The result is odd")