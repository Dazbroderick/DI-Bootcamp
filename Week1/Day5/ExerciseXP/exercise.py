     
# Exercise 1 : Convert lists into dictionaries
# Convert the two following lists, into dictionaries.

# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]

# new_dictionary = dict(zip(keys, values))
# print(new_dictionary)




#  Exercise 2 : Cinemax #2
# if a person is under the age of 3, the ticket is free.
# if they are between 3 and 12, the ticket is $10.
# if they are over the age of 12, the ticket is $15.

# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

# How much does each family member have to pay ?

# for key, value in family.items():
#     if value >= 12:
#         print(f"{key} owes $15") 
#     elif 12 >= value >= 3:
#         print(f"{key} owes $10")

# Print out the family’s total cost for the movies.
    
# how_much_owed = 0

# for value in family.values():
#     if value >= 12:
#         how_much_owed += 15
#     elif 12 >= value >= 3:
#         how_much_owed += 10
    
# print(how_much_owed)    

# Bonus: Ask the user to input the names and ages instead of using the provided family variable (Hint: ask the user for names and ages and add them into a family dictionary that is initially empty).

# family_key = []
# family_value = []

# for i in range (3):
#     family_key_name = input("Please write your name: ")
#     family_key.append(family_key_name)
#     family_value_age = int(input("Please write your age: "))
#     family_value.append(family_value_age)
    
# new_family_dictionary = dict(zip(family_key,family_value))
# print(new_family_dictionary)

# for key, value in new_family_dictionary.items():
#     if value >= 12:
#         print(f"{key} owes $15") 
#     elif 12 >= value >= 3:
#         print(f"{key} owes $10")
    
# how_much_owed = 0
# for value in new_family_dictionary.values():
#     if value >= 12:
#         how_much_owed += 15
#     elif 12 >= value >= 3:
#         how_much_owed += 10
    
# print(how_much_owed)    




# # Exercise 3: Zara
# # 1. Here is some information about a brand.

# # name: Zara 
# # creation_date: 1975 
# # creator_name: Amancio Ortega Gaona 
# # type_of_clothes: men, women, children, home 
# # international_competitors: Gap, H&M, Benetton 
# # number_stores: 7000 
# # major_color: 
# #     France: blue, 
# #     Spain: red, 
# #     US: pink, green


# # 2. Create a dictionary called brand which value is the information from part one (turn the info into keys and values).
# # The values type_of_clothes and international_competitors should be a list. The value of major_color should be a dictionary.

# brand = {
#     "name": "Zara",
#     "creation_date": 1975,
#     "creator_name": "Amancio Ortega Gaona",
#     "type_of_clothes": ["men", "women", "children", "home"],
#     "international_competitors": ["Gap", "H&M", "Benetton"],
#     "number_stores": 7000, 
#     "major_color": { 
#         "France": "blue", 
#         "Spain": "red", 
#         "US": ["pink", "green"]}

# }

# # 3. Change the number of stores to 2.

# brand['number_stores'] = 2


# # 4. Use the key [type_of_clothes] to print a sentence that explains who Zaras clients are.

# type_of_clothes_string = ", ".join(brand["type_of_clothes"])
# print(f"Zara's clients are {type_of_clothes_string}")


# # 5. Add a key called country_creation with a value of Spain.

# brand['country_creation'] = "Spain"
# print(brand["country_creation"])


# # 6. Check if the key international_competitors is in the dictionary. If it is, add the store Desigual.

# if "international_competitors" in brand:
#     brand["international_competitors"].append("Desigual")
# print(brand["international_competitors"])

# # 7. Delete the information about the date of creation.

# del brand["creation_date"]

# # 8. Print the last international competitor.

# print(brand["international_competitors"][-1])

# # 9. Print the major clothes colors in the US.

# print(brand["major_color"]["US"])

# # 10. Print the amount of key value pairs (ie. length of the dictionary).

# print(len(brand))

# # 11. Print the keys of the dictionary.

# print(brand.keys())

# # 12. Create another dictionary called more_on_zara with the following details:

# # creation_date: 1975 
# # number_stores: 10 000

# more_on_zara = {
#     "creation_date": 1975,
#     "number_stores": 10000,
# }

# print(more_on_zara)

# # 13. Use a method to add the information from the dictionary more_on_zara to the dictionary brand.

# brand.update(more_on_zara)
# print(brand)

# # 14. Print the value of the key number_stores. What just happened?

# print(brand["number_stores"])
# # the number changed from 2 to 1000.




# Exercise 4 : Disney characters
# Use this list :

users = ["Mickey","Minnie","Donald","Ariel","Pluto"]

# Analyse these results :

#1/ >>> print(disney_users_A)
# {"Mickey": 0, "Minnie": 1, "Donald": 2, "Ariel": 3, "Pluto": 4}

#2/ >>> print(disney_users_B)
# {0: "Mickey",1: "Minnie", 2: "Donald", 3: "Ariel", 4: "Pluto"}

#3/ >>> print(disney_users_C)
# {"Ariel": 0, "Donald": 1, "Mickey": 2, "Minnie": 3, "Pluto": 4}


# 1. Use a for loop to recreate the 1st result. Tip : don’t hardcode the numbers.
    
disney_users = []
disney_users_index = 0
for user in users:
    disney_users.append(disney_users_index)
    disney_users_index += 1

disney_users_A = dict(zip(users,disney_users))
print(disney_users_A)

# 2. Use a for loop to recreate the 2nd result. Tip : don’t hardcode the numbers.

disney_users_B = dict(zip(disney_users,users))
print(disney_users_B)
    
# 3. Use a method to recreate the 3rd result. Hint: The 3rd result is sorted alphabetically.

users.sort()
disney_users_C = dict(zip(users,disney_users))
print(disney_users_C)



# 4. Only recreate the 1st result for:
# The characters, which names contain the letter “i”.

# only_letter_i = []

# for user in users:
#    for char in user:
#         if char == "i":
#              only_letter_i.append(user)

only_letter_i =[user for user in users if "i"
               in user]

disney_users_A_2 = {user: index for index, user in enumerate(only_letter_i)}
print(disney_users_A_2)


# The characters, which names start with the letter “m” or “p”.


# only_letter_m_p = []

# for user in users:
#         if user.lower().startswith(("m","p")):
#              only_letter_m_p.append(user)


only_letter_m_p =[user for user in users if "m"
               in user[0].lower() or "p" in user[0].lower()]

disney_users_A_3 = {user: index for index, user in enumerate(only_letter_m_p)}
print(disney_users_A_3)
