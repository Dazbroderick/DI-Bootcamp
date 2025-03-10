#Exercise 1 
print("Hello world "*4, "I love python "*4)
     
# Exercise 2
month = int(input("Please choose pick a month from 1 to 12: "))

if 3 <= month <= 5: 
    print ("The season is Spring.")
elif 6 <= month <= 8:
    print ("The season is Summer.")
elif 9 <= month <= 11:
    print ("The season is Autumn.")
elif 1 <= month <= 2 or month == 12:
    print ("The season is Winter.")
else:
    print("Please choose a number from 1 to 12")