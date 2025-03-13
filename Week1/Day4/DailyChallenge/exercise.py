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

user_string = input("Please write a string: ")
new_string = user_string[0]

for letter in range(1, len(user_string)):
    if user_string[letter] != user_string[letter - 1]:
        new_string += user_string[letter]

print(new_string)