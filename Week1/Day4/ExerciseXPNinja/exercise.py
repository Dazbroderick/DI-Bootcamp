# # Exercise 1     
# import math

# C = 50
# H = 30


# sequence = input("Please enter numbers separated by commas: ")
# sequence_list = sequence.split(",")

# # convert to integer:
# sequence_integers = []
# for number in sequence_list:
#     sequence_integers.append(int(number))
# # alternatively:
# # sequence_integers = [int(number) for number in sequence_list]


# calculation = []
# for num in sequence_integers:
#     D = num
#     Q = math.sqrt((2 * C * D)/H)
#     calculation.append(int(Q))

# print(calculation)

# # Exercise 2     

list_of_numbers = [18, 19, 2, 56, 33, 17, 41, -63, -82, 1]

# print(list_of_numbers)

# list_of_numbers.sort()
# list_of_numbers.reverse()
# print(list_of_numbers)

# print(sum(list_of_numbers))


# list_of_numbers_2 = []
# list_of_numbers_2.append(list_of_numbers.pop(0))
# list_of_numbers_2.append(list_of_numbers.pop(-1))
# print(list_of_numbers_2)


# list_of_numbers_3 = []
# for number in list_of_numbers:
#     if number > 50:
#         list_of_numbers_3.append(number)
# print(list_of_numbers_3)


# list_of_numbers_4 = []
# for number in list_of_numbers:
#     if number < 10:
#         list_of_numbers_4.append(number)
# print(list_of_numbers_4)
# # Alternatively:
# list_of_numbers_4 = [number for number in list_of_numbers if number < 10]
# print(list_of_numbers_4)


# list_of_numbers_5 = []
# for number in list_of_numbers:
#     list_of_numbers_5.append(number*number)
# print(list_of_numbers_5)


# list_of_numbers_6 = []
# for number in list_of_numbers:
#      if number not in list_of_numbers_6:
#         list_of_numbers_6.append(number)
# print(list_of_numbers_6)
# print(len(list_of_numbers_6))



# average = (sum(list_of_numbers)/len(list_of_numbers))
# print(average)



# print(max(list_of_numbers))
# print(min(list_of_numbers))


# list_of_numbers_sum = 0
# for number in list_of_numbers:
#     list_of_numbers_sum += number
# print(list_of_numbers_sum)


# list_of_numbers.sort()
# print(list_of_numbers.pop(0))
# print(list_of_numbers.pop(-1))



# list_of_numbers_7 = []
# for i in range(10):
#     choose_your_number = int(input("Choose a number between -100 and 100: "))
#     list_of_numbers_7.append(choose_your_number)
# print(list_of_numbers_7)

        

import random

# list_of_numbers_8 = []
# for i in range(10):
#     number = random.randint(-100,100)    
#     list_of_numbers_8.append(number)
# print(list_of_numbers_8)



# list_of_numbers_9 = []
# random_range = random.randint(1,100)
# for i in range(random_range):
#     number = random.randint(-100,100)
#     list_of_numbers_9.append(number)
# print(list_of_numbers_9)



# Exercse 3     

random_paragraph = "The shoes had been there for as long as anyone could remember. In fact, it was difficult for anyone to come up with a date they had first appeared. It had seemed they'd always been there and yet they seemed so out of place. Why nobody had removed them was a question that had been asked time and again, but while they all thought it, nobody had ever found the energy to actually do it. So, the shoes remained on the steps, out of place in one sense, but perfectly normal in another."

# How many characters it contains (this one is easy…).

print(len(random_paragraph))

# How many sentences it contains.

end_count = []

sentences = random_paragraph.split('.')
for sentence in sentences:
    stripped_sentence = sentence.strip()
    if sentence.strip():
        end_count.append(stripped_sentence)
        
print(len(end_count))


# How many words it contains.

sentences_words = random_paragraph.split(' ')
print(len(sentences_words))


# How many unique words it contains.

new_random_paragraph = random_paragraph.replace(",","").replace(".","")
random_paragraph_list = new_random_paragraph.split()
non_unique_words = set(random_paragraph_list)

print(len(sentences_words) - len(non_unique_words))


# Bonus: How many non-whitespace characters it contains.

whitsespace_count = 0
for char in random_paragraph:
    if not char.isspace():
        whitsespace_count += 1
print(whitsespace_count)

# Bonus: The average amount of words per sentence in the paragraph.



avg_words_in_sentence = (len(sentences_words)/len(end_count))
print(avg_words_in_sentence)


# Bonus: the amount of non-unique words in the paragraph.


new_random_paragraph = random_paragraph.replace(",","").replace(".","")
random_paragraph_list = new_random_paragraph.split()
non_unique_words = set(random_paragraph_list)
print(len(non_unique_words))

# Exercise 4
# Write a program that prints the frequency of the words from the input.

following_input = "New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3."

just_the_words = following_input.split(' ')

for word in just_the_words:
    the_word_count = just_the_words.count(word)
    print(f"{word}:{the_word_count}")




