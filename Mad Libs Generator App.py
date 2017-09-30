"""
Aim of the app is to take user input and place it into a pre-made story
First take user input for Name, Age, Course, Country
Print out the story at the end
"""

name = input("What is your name: ")
age = input("What is your age: ")
course = input("What course are you studying: ")
country = input("What country do you live in: ")

story = f"Hello my name is {name}, I am {age} years old and live in {country}"

print(story)

