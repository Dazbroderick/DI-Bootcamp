# Ask a user for a word
# Write a program that creates a dictionary. This dictionary stores the indexes of each letter in a list.

# Make sure the letters are the keys.
# Make sure the letters are strings.
# Make sure the indexes are stored in a list and those lists are values.


# ask_for_word = input("Please write a word: ")

# index_list = {}

# for index, char in enumerate(ask_for_word):
#     if char in index_list:
#         index_list[char].append(index)
#     else:
#         index_list[char] = [index]

# print(index_list)



# Challenge 2
# Create a program that prints a list of the items you can afford in the store with the money you have in your wallet.
# Sort the list in alphabetical order.
# Return “Nothing” if you can’t afford anything from the store.
# Hint : make sure to convert the amount from dollars to numbers. Create a program that deletes the $ sign, and the comma (for thousands)

# items_purchase = {
#   "Water": "$1",
#   "Bread": "$3",
#   "TV": "$1,000",
#   "Fertilizer": "$20"
# }

# wallet = "$300"

items_purchase = {
  "Apple": "$4",
  "Honey": "$3",
  "Fan": "$14",
  "Bananas": "$4",
  "Pan": "$100",
  "Spoon": "$2"
}

wallet = "$100" 

# items_purchase = {
#   "Phone": "$999",
#   "Speakers": "$300",
#   "Laptop": "$5,000",
#   "PC": "$1200"
# }

# wallet = "$1" 

wallet_integer = int(wallet.replace("$","").replace(",",""))

items_purchase_integer = []

for item, price in items_purchase.items():
    price_int = int(price.replace("$","").replace(",",""))
    if price_int <= wallet_integer:
        items_purchase_integer.append(item)
        items_purchase_integer.sort()

if items_purchase_integer == []:
    print("Nothing.")
else:
    print(items_purchase_integer)