# Exercise 3
# 3 <= 3 < 9  True
# 3 == 3 == 3 True
# bool(0)     False
# bool(5 == "5") False
# bool(4 == 4) == bool("4" == "4") True
# bool(bool(None)) False


# x = (1 == True) 
# y = (1 == False)
# a = True + 4
# b = False + 10

# print("x is", x) x is true
# print("y is", y) y is false
# print("a:", a) a:5
# print("b:", b)  b:10

# Exercise 4
my_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

print(len(my_text))



# Exercise 5 

previous_length = 0

keepasking = range(0,5)

for i in keepasking:
    long = input("Please input the longest sentence you can without using the letter \"A\": ")
    current_length = len(long)
    if current_length > previous_length: 
        print("Congratulations on a longer message!")
        previous_length = current_length
    else:
        print("This one isn't longer")