# # Timed Challenge #1

# reverseinp = input("Please enter a string: ")

# words = reverseinp.split()
# reversed = " ".join(words[::-1])

# print(reversed) 

# Timed Challenge #2

x = int(input('Enter the Number: ')) 

sum_of_numbers = 0

for i in range(1,x-1):
    if x % i == 0:
        sum_of_numbers += i

if sum_of_numbers == x:
    print("True")
else:
    print("False")