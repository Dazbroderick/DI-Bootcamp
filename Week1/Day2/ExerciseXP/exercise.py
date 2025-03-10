#Exercise 1 
print("Hello world "*4)


#Exercise 2
print((99**3*8))


#Exercise 3 
# 5 < 3   False
# 3 == 3  True
# 3 == "3"    False
# "3" > 3     TypeError
# "Hello" == "hello"  False


#Exercise 4 
computer_brand = "Dell"
print(f"I have a {computer_brand} computer")

#Exercise 5 
name = "Daniel"
age = 29
shoe_size = 44
info = (f"My name is {name}, and I am {age} years old. My shoe size is {shoe_size}, and you know what they say about medium size feet ;")
print(info)



#Exercise 6 
a = 10
b = 20
if a > b:
    print("Hello world")
else:
    print("The value you are looking for is false")


#Exercise 7 
odd_even = int(input("Please choose a number: "))

if odd_even % 2 == 0:
    print("The number you have chosen is even.")
else:
    print("Thats odd...")

#Exercise 8 
same_name = input("What is your name? ")

if same_name == name: 
    print("Eureka, we must be twins separated at birth who magically have been given the same name!!")
else:
    print("We can still be friends.")


#Exercise 9
height = int(input("How tall are you in centimeters? "))

if height <= 145:
    print("You need to drink some growth potion if you want to ride.")
else:
    print("You have been deemed tall enough by the gods to ride!")



 
 