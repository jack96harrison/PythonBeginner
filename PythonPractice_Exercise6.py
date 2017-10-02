"""
Asks the user to input a string and tells them if it is a palindrome

"""

user_string = (str(input("Please enter a palindrome: ")))

user_list = []

for letter in user_string:
    user_list.append(letter)

user_list.reverse()

user_string_reversed = ""

for letter in user_list:
    user_string_reversed += letter

if user_string == user_string_reversed:
    print("Well done you entered a palindrome")
else:
    print("Oops you didn't enter a palindrome")
