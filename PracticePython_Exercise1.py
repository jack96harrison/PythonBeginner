"""
Build a program which asks the user to enter their name and age
Print a message to them telling them when they will be 100
"""
name = input("What is your name? ")
age = input("How old are you? ")
age = int(age)

years_to_hundred = 100 - age

sentence = f"Hello {name}, you are currently {age} years old. You will be 100 in {years_to_hundred} years."

print(sentence)
