# #Exercise 1

# list_1 = [1,2,3,4,5]
# list_2 = [6,7,8,9]
# list_1.extend(list_2)
# print(list_1)




# #Exercise 2
# range_1 = range(1500,2500)
 

# for multiple_of_5 in range_1:
#     if multiple_of_5%5 == 0 or multiple_of_5%7 ==0:
#         print(multiple_of_5)




# #Exercise 3
# names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']

# user_name = input("What is your name? ")

# for name in names:
#     if name == user_name:
#         print(f"{user_name} is at index {names.index(name)}")





# #Exercise 4

# numbers = []

# for attempt in range(1,4):
#     input_numbers = int(input("Please input a number: "))
#     numbers.append(input_numbers)

# numbers.reverse()
# print(f"The greatest number is: {numbers.pop(0)}")





# #Exercise 5

# alphabet = "abcdefghijklmnopqrstuvwxyz"

# for char in alphabet:
#     if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
#         print(f"{char} is a vowel")
#     else:
#         print(f"{char} is a consonant")





# #Exercise 6

# single_character = input("Please input a single character: ")

# words = []

# for word in range(3):
#     seven_words = input("Please input a word: ")
#     words.append(seven_words)

# for word in words:
#         if single_character in word:
#             print(f"The index of the character you chose is {word.index(single_character)}")
#         else:
#              print(f"Sorry, {single_character} isn't found in the word {word}")
        




# #Exercise 7
# one_million = []

# for i in range(1, 1000001):
#     one_million.append(i)

# # Or
# # one_million = list(range(1, 1000001))

# print(min(one_million))
# print(max(one_million))
# print(sum(one_million))




# #Exercise 8

# sequence = input("Please enter numbers separated by commas: ")

# sequence_list = sequence.split(",")
# print(sequence_list)

# sequence_tuple = tuple(sequence_list)
# print(sequence_tuple)





# #Exercise 9
# import random

# random_number = random.randint(1,9)

# total_wins = 0
# total_losses = 0

# while True:
#     user_input = input("Please input a number from 1 to 9 (press 'q' to quit): ")
#     if user_input == 'q':
#         break
#     elif user_input == random_number:
#        total_wins += 1
#        print("Winner!")
#     else:
#         print("Loser!")
#         total_losses += 1

# print(f"Total wins: {total_wins}\nTotal losses: {total_losses}")