# matrix = '''7ii
# Tsx
# h%?
# i #
# sM 
# $a 
# #t%
# ^r!'''


# matrix_1 = list(matrix)
# matrix_2 = []

# for i in matrix_1:
#     if i != "\n":
#         matrix_2.append(i)

# # create separate lists of three characters within a bigger list.
# def split_every_three(my_list):
#     return [my_list[i:i+3] for i in range(0, len(my_list), 3)]

# matrix_3 = split_every_three(matrix_2)

# # extract the first/second/third characters of each sublist and put them into their own lists.
# def slice_list(matrix_3):
#     first_char = [first[0] for first in matrix_3]
#     second_char = [first[1] for first in matrix_3]
#     third_char = [first[2] for first in matrix_3]

#     return [first_char, second_char, third_char]

# matrix_4 = slice_list(matrix_3)

# # turn everything into one list.
# matrix_5 =[]
# for sublist in matrix_4:
#     for item in sublist:
#         matrix_5.append(item)

# matrix_6 = []
# for i in range(len(matrix_5)):
#     if matrix_5[i].isalpha():
#         matrix_6.append(matrix_5[i])
#     else:
#         matrix_6.append(" ")

# matrix_7 = []
# for i in range(len(matrix_6)):
#     if matrix_6[i] == " " and matrix_6[i-1] != " ":
#         matrix_7.append(" ")
#     elif matrix_6[i] != " ":
#         matrix_7.append(matrix_6[i])


# final_message = "".join(matrix_7)
# print(final_message)




# # # # ChatGPT's answer: 

# # matrix = [
# #     "7ii",
# #     "Tsx",
# #     "h%?",
# #     "i #",
# #     "sM ",
# #     "$a ",
# #     "#t%",
# #     "^r!"
# # ]

# # # Step 1: Create an empty string to store the decrypted message.
# # decrypted_message = ""

# # # Step 2: Loop through each column (i.e., loop through characters in each row)
# # for col in range(len(matrix[0])):
# #     # Step 3: Loop through each row and get the character from the current column
# #     for row in matrix:
# #         # Add the character to the decrypted message if it is an alphabetic character
# #         if row[col].isalpha():
# #             decrypted_message += row[col]

# # # Step 4: Replace symbols between alphabetic characters with spaces.
# # # We can use regular expressions to replace groups of non-alphabetic characters
# # import re
# # decrypted_message = re.sub(r'[^a-zA-Z]+', ' ', decrypted_message)

# # # Step 5: Print the decrypted message
# # print(decrypted_message)

simple_dict = {
    'a': 2,
    'b': 4
}

my_dict = {key:value**2 for key,value in simple_dict.items() if value%2==0}

print(my_dict)
