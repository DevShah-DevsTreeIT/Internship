# Map()
# syntax:-map(lambda_function, iterable)

num = [1,2,3,4,5,6]

square = list(map(lambda x : x * x,num))
print(f"This is the square of numbers using map():  {square}")

numbers = [1, 2, 3, 4, 5]

doubled = list(map(lambda x: x * 2, numbers))
print(f"This is the double of numbers Using the  one and only map(): {doubled}")  # [2, 4, 6, 8, 10]

# Filter
# syntax:- filter(lambda_function, iterable)

numbers = [1, 2, 3, 4, 5, 6]

evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers  = ",evens)


# words = []
words = ["HEy","Hello","hiiii"]

long_words = list(filter(lambda word : len(word)>3,words))

print(long_words)


#####################3lambda word: len(word) > 3 → checks if each word is longer than 3 characters
# 
# filter(...) → keeps only the words that match the condition
# 
# list(...) → turns the result into a usable list


# sorted()
# syntax :- sorted(iterable, key=lambda_function)

students = [("Alice", 90), ("Bob", 80), ("Charlie", 95)]

sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)
# [('Bob', 80), ('Alice', 90), ('Charlie', 95)]
#########
fruits = ["banana", "apple", "pear", "grape"]

sorted_fruits = sorted(fruits, key=lambda fruit: len(fruit))
sorted_fruits1 = sorted(fruits, key=lambda fruit: len(fruit),reverse=True)

print(sorted_fruits)
print(sorted_fruits1)

#########
people = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35}
]



sorted_age = sorted(people,key =lambda person: person['age']  )
print(sorted_age)