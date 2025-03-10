
description = "strings are..."

# make it all upper case
# replace the word "are" to "is"
# print just the word "strings"

print(description.upper())
print(description.replace("are", "is"))
print(description.replace("are...", ""))
print(description.split()[0])

# Given the following values:

# x = 5
# y = 10
# z = 0
# word1 = "hello"
# word2 = "world"

# 1. Check if x is less than y and y is greater than z.

# 2. Verify if word1 is not equal to word2.

# 3. Use the bool() function to check the boolean value of z and word1.

# name = input("Please enter your name: ")

# if len(name) < 5:
#     print("You have a short name")
# else:
#     print("Nice name bro!")


# Ask the user for a number between 1 and 100

# If the number is a multiple of three, print Fizz

# If the number is a multiple of five, print Buzz.

# If the number is a multiple is a multiples of both three and five, print FizzBuzz instead.

number = int(input("Please write a number between 1 and 100: "))

if number % 15 == 0:
    print("FizzBuzz")
elif number % 5 == 0:
    print("Buzz")
else: 
    number % 3 == 0
    print("Fizz")

