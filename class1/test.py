# l = ['apple', 'banana', 'cherry', 35, [ 'one', [1,2,3,4], 'three' ] ]

# when list inside a list -> nexted list
# print(list[4][1][2])  # output -> two

# d = {
#     'name': 'akhilesh',
#     'age': 35,
#     'city': 'bangalore',
#     'skills': ['python', 'devops', 'aws'],
#     'education': [{'college': 'nit'}, {'school': 'high school'}]

# }

# # print(dict['students'])  # KeyError
# print(dict.get('education', None)[0].get('college'))


# tuples

# tuple_data = ('apple', 'banana', 'cherry', 35) 

# # print(tuple_data[2])  # output -> cherry
# first,secnd,third,forth = tuple_data

# print(secnd)  # output -> banana
# conditipnals 

# if 10 == 5:
#     print("10 is greater than 5")
# elif 10 == 19:
#     print("10 is equal to 10")
# else:
#     print("none f thema are true")


# if 'bananaa' in list:
#     print("banana is present in the list")
# elif 'grapes' in list:
#     print("grapes is present in the list")
# else:
#     print("none of the items are present")


# l = ['day1', 'day2', 'day3', 'day4']
# d = {'name': 'akhilesh', 'age': 35}

# if isinstance(d, list):
#     print(d[0])

# elif isinstance(d, dict):
#     print(d.get('name'))


# loops 
# - if you want to do some thikng multiple times
# you want to go through each item in a collection (list, dict, set, tuple)

# for i in range(5):
#     print("hello world", i)

# for i in range(5, 25, 3):
#     print("hello world", i)


# for item in l:
#     print("item is:", item)


# for key, value in d.items():
#     print(f"key is: {key} and value is: {value}")

# for key,value in d.items():
#     print(f'kye of dic is: {key} and value is: {value}')


# Functions

# def add_fun(a, b):
#     c = a + b
#     return("sum is:", c)

# output = add_fun(3,6)
# print(output)


# def greet(greeting="Hello", name="Guest"):
#     return f"{greeting}, {name}! \n Welcome to Python for DevOps Bootcamp."

# print(greet()) 
# print(greet(name="Akhilesh", greeting="YO Yo"))  # Output: Hello, Akhilesh!


