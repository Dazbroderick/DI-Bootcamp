# # Exercise 1 : Student Grade Summary
# # Requirements:
# # Calculate the average grade for each student and store the results in a new dictionary called student_averages.


# student_grades = {
#     "Alice": [88, 92, 100],
#     "Bob": [75, 78, 80],
#     "Charlie": [92, 90, 85],
#     "Dana": [83, 88, 92],
#     "Eli": [78, 80, 72]
# }

# student_averages = {}
# student_letter_grades = {}

# for name, grade in student_grades.items():
#     student_averages[name] = sum(grade)/len(grade)
# print(student_averages)

# # Assign each student a letter grade (A, B, C, D, F) based on their average grade according to the following scale, and store the results in a dictionary called student_letter_grades:
# # A: 90 and above
# # B: 80 to 89
# # C: 70 to 79
# # D: 60 to 69
# # F: Below 60

# for name, grade in student_averages.items():
#     if grade >= 90:
#         student_letter_grades[name] = "A"
#     if 79 < grade < 90:
#         student_letter_grades[name] = "B"
#     if 69 < grade < 80:
#         student_letter_grades[name] = "C"
#     if 59 < grade < 70:
#         student_letter_grades[name] = "D"
#     if grade < 60:
#         student_letter_grades[name] = "F"

# print(student_letter_grades)

# # Calculate the class average (the average of all students’ averages) and print it.

# class_average = 0
# number_of_students = 0

# for name, grade in student_averages.items():
#     class_average += grade
#     number_of_students += 1

# print(class_average/number_of_students)


# # Print the name of each student, their average grade, and their letter grade.

# for name in student_grades.keys():
#     print(f"{name}: Average grade = {student_averages[name]}, Letter grade = {student_letter_grades[name]}")



# # finding the length of the longest name.
# max_name_length = max(len(name) for name in student_grades.keys())

# # Which lets you add sapces in front of each name such that all the average grades start from the same line. also you can set it so that only a couple of decimal points are shown, for a more clean text:
# for name in student_grades.keys():
#     spaces = ' ' * (max_name_length - len(name))
#     print(f"{name}:{spaces} Average Grade = {student_averages[name]:.2f}, Letter Grade = {student_letter_grades[name]}")







# Exercise 2 : Advanced Data Manipulation and Analysis
# In this exercise, you will analyze data from a hypothetical online retail company to gain insights into sales trends and customer behavior. The data is represented as a list of dictionaries, where each dictionary contains information about a single purchase.

sales_data = [
    {"customer_id": 1, "product": "Smartphone", "price": 600, "quantity": 1, "date": "2023-04-03"},
    {"customer_id": 2, "product": "Laptop", "price": 1200, "quantity": 1, "date": "2023-04-04"},
    {"customer_id": 1, "product": "Laptop", "price": 1000, "quantity": 1, "date": "2023-04-05"},
    {"customer_id": 2, "product": "Smartphone", "price": 500, "quantity": 2, "date": "2023-04-06"},
    {"customer_id": 3, "product": "Headphones", "price": 150, "quantity": 4, "date": "2023-04-07"},
    {"customer_id": 3, "product": "Smartphone", "price": 550, "quantity": 1, "date": "2023-04-08"},
    {"customer_id": 1, "product": "Headphones", "price": 100, "quantity": 2, "date": "2023-04-09"},
]

# 1. Total Sales Calculation: Calculate the total sales for each product category (i.e., the total revenue generated from each type of product). Use a loop to iterate through the data and a dictionary to store the total sales for each product.

total_sales = {}
for data_of_sales in sales_data:
    product = data_of_sales["product"]
    total_revenue = data_of_sales["price"] * data_of_sales["quantity"]
    if product in total_sales:
        total_sales[product] += total_revenue
    else:
        total_sales[product] = total_revenue
print(total_sales)
        

# 2. Customer Spending Profile: Determine the total amount spent by each customer. Use a dictionary to maintain the sum of amounts each customer has spent.

customer_spending = {}
for data_of_sales in sales_data:
    customer_id = data_of_sales["customer_id"]
    total_revenue = data_of_sales["price"] * data_of_sales["quantity"]
    if customer_id in customer_spending:
        customer_spending[customer_id] += total_revenue
    else:
        customer_spending[customer_id] = total_revenue

print(customer_spending)

# 3. Sales Data Enhancement:
# Add a new field to each transaction called “total_price” that represents the total price for that transaction (quantity * price).
# Use a loop to modify the sales_data list with this new information.

for data_of_sales in sales_data:
    data_of_sales["total_price"] = data_of_sales["price"] * data_of_sales["quantity"]
    
print(sales_data)

# 4. High-Value Transactions:
# Using list comprehension, create a list of all transactions where the total price is greater than $500.
# Sort this list by the total price in descending order.

all_transactions_greater_than_500 = [transaction for transaction in sales_data if transaction["price"] * transaction["quantity"] > 500]

all_transactions_greater_than_500.sort(key=lambda x: x["price"] * x["quantity"], reverse=True)
print(all_transactions_greater_than_500)

# 5. Customer Loyalty Identification:
# Identify any customer who has made more than one purchase, suggesting potential loyalty.
# Use a dictionary to count purchases per customer, then use a loop or comprehension to identify customers meeting the loyalty criterion.

purchase_count = {}
for data_of_sales in sales_data:
    customer_id = data_of_sales["customer_id"]
    if customer_id in purchase_count:
        purchase_count[customer_id] += 1
    else:
        purchase_count[customer_id] = 1

loyal_customers = []
for customer_id, purchases in purchase_count.items():
    if purchases > 2:
        loyal_customers.append(customer_id)

print(purchase_count)


# 6. Bonus: Insights and Analysis:
# Calculate the average transaction value for each product category.
# Identify the most popular product based on the quantity sold.
# Provide insights into how these analyses could inform the company’s marketing strategies.