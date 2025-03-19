# Exercise 1 : What are you learning ?
# Write a function called display_message() that prints one sentence telling everyone what you are learning in this course.
# Call the function, and make sure the message displays correctly.

# def display_message():
#     print ("I am learning Full Stack Web Developement at DI.")

# display_message()


# 🌟 Exercise 2: What’s your favorite book?
# Write a function called favorite_book() that accepts one parameter called title.
# The function should print a message, such as "One of my favorite books is <title>".
# For example: “One of my favorite books is Alice in Wonderland”
# Call the function, make sure to include a book title as an argument when calling the function.


# def favorite_book(title):
#     print(f"One of my favorite books is {title}!")

# favorite_book("Harry Potter")


# 🌟 Exercise 3 : Some Geography
# Write a function called describe_city() that accepts the name of a city and its country as parameters.
# The function should print a simple sentence, such as "<city> is in <country>".
# For example “Reykjavik is in Iceland”
# Give the country parameter a default value.
# Call your function.

# def describe_city(city, country="Israel"):
#     print(f"{city} is in {country}!")

# describe_city("Shaalvim")


# Exercise 4 : Random
# Create a function that accepts a number between 1 and 100 and generates another number randomly between 1 and 100. Use the random module.
# Compare the two numbers, if it’s the same number, display a success message, otherwise show a fail message and display both numbers.

# import random

# def accept_num():
#     pick_random = int(input("pick a number from 1 to 100: "))
#     random_number = random.randint(1,100)

#     # print(pick_random)
#     # print(random_number)

#     if pick_random == random_number:
#         print("Success!")    
#     else:
#         print("Failure!")


# accept_num()



# # 🌟 Exercise 5 : Let’s create some personalized shirts !
# # 1. Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt.
# # The function should print a sentence summarizing the size of the shirt and the message printed on it, such as "The size of the shirt is <size> and the text is <text>"
# # Call the function make_shirt().

# def make_shirt():
#     size = input("Please enter a size: ")
#     text = input("Please enter text you want on the shirt: ")
#     print(f"The size of the shirt is {size} and the text is {text}")

# make_shirt()


# # 2. Modify the make_shirt() function so that shirts are large by default with a message that reads “I love Python” by default.
# # Call the function, in order to make a large shirt with the default message


# def make_shirt(size="Large",text="I love Python"):
#     print(f"The size of the shirt is {size} and the text is {text}")

# make_shirt()

# # 3. Make medium shirt with the default message

# def make_shirt(size="Medium",text="I love Python"):
#     print(f"The size of the shirt is {size} and the text is {text}")

# make_shirt()

# # 4. Make a shirt of any size with a different message.


# def make_shirt(size="Small",text="The name is Python, Monty Python."):
#     print(f"The size of the shirt is {size} and the text is {text}")

# make_shirt()

# # 5. Bonus: Call the function make_shirt() using keyword arguments.

# def make_shirt(size,text):
#     print(f"The size of the shirt is {size} and the text is {text}")

# make_shirt(size="Small",text="The name is Python, Monty Python.")



# #  Exercise 6 : Magicians

# magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

# # 1.	Create a function called show_magicians(), which prints the name of each magician in the list.

# def show_magicians(magicians):
#     for magician in magicians:
#         print(magician)

# show_magicians(magician_names)


# # 2.	Write a function called make_great() that modifies the original list of magicians by adding the phrase "the Great" to each magician’s name.
# # 3.	Call the function make_great().


# def make_great(magicians):
#     for magician in range(len(magicians)):
#         magicians[magician] = "The Great " + magicians[magician]

# make_great(magician_names)


# # 4.	Call the function show_magicians() to see that the list has actually been modified.

# show_magicians(magician_names)





# 🌟 Exercise 7 : Temperature Advice
# 1.	Create a function called get_random_temp().
    # 1.	This function should return an integer between -10 and 40 degrees (Celsius), selected at random.
    # 2.	Test your function to make sure it generates expected results.

# import random

# def get_random_temp():
#     return random.randint(-10,40)
    
# print(f"{get_random_temp()} degrees Celsius")

# 2.	Create a function called main().
    # 1.	Inside this function, call get_random_temp() to get a temperature, and store its value in a variable.
    # 2.	Inform the user of the temperature in a friendly message, eg. “The temperature right now is 32 degrees Celsius.”


# def main():
#     random_temperature = get_random_temp()
#     print(f"The temperature right now is {get_random_temp()} degrees Celsius")

# main()


# 3.	Let’s add more functionality to the main() function. Write some friendly advice relating to the temperature:
    # 1.	below zero (eg. “Brrr, that’s freezing! Wear some extra layers today”)
    # 2.	between zero and 16 (eg. “Quite chilly! Don’t forget your coat”)
    # 3.	between 16 and 23
    # 4.	between 24 and 32
    # 5.	between 32 and 40

# def main():
#     random_temperature = get_random_temp()
#     if random_temperature < 0:
#         print(f"Brrr, that’s freezing! Wear some extra layers today")
#     elif 0 <= random_temperature <= 16:
#         print(f"Quite chilly! Don’t forget your coat")
#     elif 17 <= random_temperature <= 23:
#         print(f"Heyo")
#     elif 24 <= random_temperature <= 31:
#         print(f"Heyooooo")
#     elif 32 <= random_temperature <= 40:
#         print(f"Heyooooooooo")


# main()


# 4.	Change the get_random_temp() function:
    # 1.	Add a parameter to the function, named ‘season’.
    # 2.	Inside the function, instead of simply generating a random number between -10 and 40, set lower and upper limits based on the season, eg. if season is ‘winter’, temperatures should only fall between -10 and 16.

# def get_random_temp(season):
#      if season == "winter":
#         return random.randint(-10,16)
#      elif season == "autumn":
#         return random.randint(17,23)
#      elif season == "spring":
#         return random.randint(24,32)
#      elif season == "summer":
#         return random.randint(33,40)
    
    # 3.	Now that we’ve changed get_random_temp(), let’s change the main() function:
        # 1.	Before calling get_random_temp(), we will need to decide on a season, so that we can call the function correctly. Ask the user to type in a season - ‘summer’, ‘autumn’ (you can use ‘fall’ if you prefer), ‘winter’, or ‘spring’.
        # 2.	Use the season as an argument when calling get_random_temp().

# pick_season = input("Please choose a season(summer, autumn, winter, or spring): ")

# print(get_random_temp(season=pick_season))


# 5.	Bonus: Give the temperature as a floating-point number instead of an integer.

# def get_random_temp(season):
#     if season == "winter":
#         return round(random.uniform(-10, 16), 2)
#     elif season == "autumn":
#         return round(random.uniform(17, 23), 2)
#     elif season == "spring":
#         return round(random.uniform(24, 32), 2)
#     elif season == "summer":
#         return round(random.uniform(33, 40), 2)

# pick_season = input("Please choose a season (summer, autumn, winter, or spring): ")
# print(get_random_temp(season=pick_season))

# 6.	Bonus: Instead of asking for the season, ask the user for the number of the month (1 = January, 12 = December). Determine the season according to the month.











# 🌟 Exercise 8 : Star Wars Quiz
# This project allows users to take a quiz to test their Star Wars knowledge.
# The number of correct/incorrect answers are tracked and the user receives different messages depending on how well they did on the quiz.
# Here is an array of dictionaries, containing those questions and answers
data = [
    {
        "question": "What is Baby Yoda's real name?",
        "answer": "Grogu"
    },
    {
        "question": "Where did Obi-Wan take Luke after his birth?",
        "answer": "Tatooine"
    },
    {
        "question": "What year did the first Star Wars movie come out?",
        "answer": "1977"
    },
    {
        "question": "Who built C-3PO?",
        "answer": "Anakin Skywalker"
    },
    {
        "question": "Anakin Skywalker grew up to be who?",
        "answer": "Darth Vader"
    },
    {
        "question": "What species is Chewbacca?",
        "answer": "Wookiee"
    }
]

# 1.	Create a function that asks the questions to the user, and check his answers. Track the number of correct, incorrect answers. Create a list of wrong_answers.

correct_answers = []
wrong_answers = []

def star_wars_quiz(quiz):
    for dictionary in quiz:
        question = dictionary["question"]
        correct_answer = dictionary["answer"]

        user_answer = input(f"{question}")

        
        if user_answer.lower() == correct_answer.lower():
            correct_answers.append(user_answer)
        else:
            wrong_answers.append(user_answer)

star_wars_quiz(data)

print(f"The correct answers are: {correct_answers}")
print(f"The wrong answers are: {wrong_answers}")


# 2.	Create a function that informs the user of his number of correct/incorrect answers.

def answer_count():
    print(f"You got {len(correct_answers)} correct!")
    print(f"You got {len(wrong_answers)} wrong!")

answer_count()

# 3.	Bonus : display to the user the questions he answered wrong, his answer, and the correct answer.
# If he had more then 3 wrong answers, ask him to play again.

