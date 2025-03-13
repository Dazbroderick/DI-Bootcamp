# # Exercise 1

# my_fav_numbers = {1,2,3,4,5,6,7,8,9}

# # my_fav_numbers.add(10)
# # my_fav_numbers.add(11)

# my_fav_numbers.update([10, 11])
# print(my_fav_numbers)

# # Removing last number

# remove_last = list(my_fav_numbers)
# remove_last.pop()
# new_fav_numbers = set(remove_last)
# print(new_fav_numbers)

# # Alternatively
# my_fav_numbers.remove(11)
# print(my_fav_numbers)

# # Concatenate two sets
# friend_fav_numbers = {13, 14, 15, 16, 17}
# our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
# print(our_fav_numbers)

# # Exercise 2
# # tuples are immutable and thus you cannot add to them.

# # Exercise 3
# basket = ["Banana", "Apples", "Oranges", "Blueberries"]

# basket.remove("Banana")
# basket.remove("Blueberries")
# basket.append("Kiwi")
# basket.insert(0, "Apples")
# basket.count("Apple")
# basket.clear()
# print(basket)

# # Exercise 4
# # A float is an integer with a decimal point.

# decimal_list = []
# decimal_point = 0.5
# for decimalpoint in range(1,5):
#     decimal_point +=1
#     decimal_list.append(decimal_point)

# numbered_list = []
# regular_integer = 1
# for wholenumber in range(1,5):
#     regular_integer +=1
#     numbered_list.append(regular_integer)


# mixed_list = (numbered_list + decimal_list)
# mixed_list.sort()
# print(mixed_list)

# # Online solution
# # numbers = [i / 2 + 1 for i in range(1, 9)]
# # print(numbers)


# # Exercise 5
# for everything in range(1,21):
#     print(everything)


# for everything in range(1,21):
#     if everything % 2 == 0:
#         print(everything)


# # Exercise 6
# name = input("Enter your name: ") 

# while name != "Daniel Broderick":
#         name = input("Enter your name: ")

# print("Good job!")
    


# # Exercise 7
# favorite_fruits = input("Please input your favorite fruits(put a space between each fruit): ")
# favorite_fruits_list = favorite_fruits.split()
# print(favorite_fruits_list)

# choose_fruits = input("Please choose a fruit: ")

# for fruits in favorite_fruits_list:
#     if fruits == choose_fruits:
#         print("You chose one of your favorite fruits! Enjoy!")
#     else:
#         print("You chose a new fruit. I hope you enjoy.")


# # Exercise 8

# first_topping = 10
# more_toppings = 2.5
# list_of_toppings = []
# while True:
#     pizza_toppings = input("Please enter a topping you would like on your pizza (enter 'quit' when you are finished): ")
#     if pizza_toppings == 'quit':
#         break
    
#     print(f"I'll add {pizza_toppings} to your pizza!")
#     list_of_toppings.append(pizza_toppings)


# print("Your toppings are: ", list_of_toppings, "The final price is: ", first_topping + (more_toppings*(len(list_of_toppings)-1)))
    

# # Exercise 9

# under3 = []
# between3_12 = []
# price3_12 = 10
# over12 = []
# price_over12 = 15

# while True:
#     person_age = int(input("What is your age? (Enter '0' when you are finished ordering.) "))
#     if person_age == 0:
#         break
#     elif 0 < person_age < 3:
#         under3.append(person_age)
#     elif 3 <= person_age <= 12:
#         between3_12.append(person_age)
#     else: 
#         person_age > 12
#         over12.append(person_age)

# total_price = len(between3_12)*price3_12+(len(over12)*price_over12)

# print(f"Your total price is ${total_price}")


# teen_names = ["Martin", "Jack", "Jill", "Jackie", "Eve", "Judith", "Grant"]
# permission_granted = []


# for name in teen_names:
#     teen_age = int(input(f"Hello {name}, how old are you? "))
#     if teen_age < 16 or teen_age > 21:
#         permission_granted.append(name)

# print(permission_granted)


# # Exercise 10

# sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]

# finished_sandwiches = []

# remove_sandwich = "Pastrami sandwich"
# while remove_sandwich in sandwich_orders:
#     sandwich_orders.remove(remove_sandwich)
# print(sandwich_orders)


# while sandwich_orders:
#     this_sandwich = sandwich_orders.pop(0)
#     finished_sandwiches.append(this_sandwich)
    
# for sandwich in finished_sandwiches:
#     print(f"I made your {sandwich}")