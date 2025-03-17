# sample_dict = { 
#    "class":{ 
#       "student":{ 
#          "name":"Mike",
#          "marks":{ 
#             "physics":70,
#             "history":80
#          }
#       }
#    }
# }

# # Access the value of the key history

# print(sample_dict["class"]["student"]["marks"]["history"])


# a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}

# print(a_dict.items())
# output : 
# dict_items([('color', 'blue'), ('fruit', 'apple'), ('pet', 'dog')])


# The items() method returns a view object that displays 
# a list of dictionary's (key, value) tuple pairs.


# for key, value in a_dict.items():
#     print(key, '->', value)



# Delete the set of keys from the python dictionary

sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"

}

keys_to_remove = ["name", "salary"]

for key in keys_to_remove:
    del sample_dict[key]

print(sample_dict)
