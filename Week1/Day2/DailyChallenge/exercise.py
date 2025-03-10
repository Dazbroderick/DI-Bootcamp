# Exercise 1
string = input("Please input a string exactly 10 characters long: ")

if len(string) < 10:
    print("The string is not long enough.")
elif len(string) > 10:
    print("The string is too long.") 
else:
    print("The string is perfect.")

# Exercise 2
    print(string[0])
    print(string[-1])

# Exercise 3
x = 1
for letter in string:
    print(string[0:x])
    x += 1

# Exercise 4
import random
shuffled = list(string)
random.shuffle(shuffled)
shuffled_string = ''.join(shuffled)
print(shuffled_string)