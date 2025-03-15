# # Challenge 1

# number = int(input("Please input a number: "))
# length = int(input("Please input a length: "))

# new_number = 0

# multiples = []
 
# while new_number < length: 
#     if number < length:
#         new_number += number
#     multiples.append(new_number)
# print(multiples)

# #Alternatively
 
# for i in range(number,length+1,number):
#     if number < length:
#         new_number += number
#     multiples.append(new_number)
# print(multiples)


# Challenge 2

# user_string = input("Please write a string: ")
# new_string = user_string[0]

# for letter in range(1, len(user_string)):
#     if user_string[letter] != user_string[letter - 1]:
#         new_string += user_string[letter]

# print(new_string)


# Daily challenge GOLD : Happy birthday
# Instructions
# Ask the user for their birthdate (specify the format, for example: DD/MM/YYYY).
# Display a little cake as seen below:


import datetime

cake =  '''
            ___iiiii___
           |:H:a:p:p:y:|
         __|___________|__
        |^^^^^^^^^^^^^^^^^|
        |:B:i:r:t:h:d:a:y:|
        |                 |
        ~~~~~~~~~~~~~~~~~~~'''

birthday = input("Please enter your birthday in the DD/MM/YYYY format: ")

birthday_year = birthday.split("/")
birthday_year_split = birthday_year[2]
birthday_year_split_final = int(birthday_year_split)

today = datetime.date.today()
today_year = today.year


how_old_you_are = (today_year) - (birthday_year_split_final)
how_old_you_are_final = (f"{how_old_you_are:02}")

number_of_candles_string = str(how_old_you_are_final)
second_digit = int(number_of_candles_string[1])


candles = ("i" * int(second_digit))
cake = cake.replace("iiiii", candles)


print(cake)
