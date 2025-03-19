def calculation_1(a,b):
    addition = a+b
    subtraction = a-b
    return addition, subtraction

res = calculation_1(40,10)
print(res)
    

def calculation_2 (a,b):  
    return(a+b, a-b)

x,y = calculation_2(40,10)
print(x)


people = ["Rick", "Morty", "Beth", "Jerry", "Snowball"]

# def less_than_4(s):
#     return len(s) <= 4

# short_name = filter(less_than_4,people)

# def say_hello(name):
#     return f"Hello {name}"

# display_names = map(say_hello, short_name)

# print(list(display_names))

short_name = filter(lambda name: len(name)<=4, people)
display_name = map(lambda name: f"Hello {name}!!", short_name)

for name in list(display_name):
    print(name)