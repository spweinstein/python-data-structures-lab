# Exercise 0: Example
#
# This is a practice exercise to familiarize you with basic Python data structures.
#
# Create a list called `example_list` and append three elements to it. Print each element using a loop.
#
# Requirements:
# - The list should contain any three elements of your choice.
# - Use a loop to print each element.

def example_list_function():
  example_list = ['element1', 'element2', 'element3']
  for element in example_list:
      print(element)

# Call the function and print each element
example_list_function()

# Exercise 1: List and Indexing
#
# Create a list named students containing at least three student names (strings).
# Assign the second student’s name to a variable named first_student.
# Assign the last student’s name to a variable named last_student.

# Updated instructions:
#Create a list named students with at least three names.
# Assign the second student (index 1) to a variable named second_student.
# Assign the last student to a variable named last_student.
# Return a tuple in this format:
# (second_student, last_student)

def manage_students():
    # your code here
    students = ["Bob", "John", "Jane"]
    second_student, last_student = students[1], students[-1]
    return second_student, last_student

# Call the function and print the result
print('Exercise 1:', manage_students())

# Exercise 2: Loop and String Concatenation
#
# Create a tuple named foods containing the same number of foods (strings) as there are names in the students list.
# Create a variable named meal and assign an empty string to it.
# Use a for loop to iterate over the strings in foods and append each string to meal.

# Updated:
# Create a tuple named foods with three food strings.
# Create a variable named meal and assign it an empty string "".
# Use a for loop to concatenate each food into meal, separated by a space.
# Return the final string.

def combine_foods():
    # your code here
    foods = ("apple", "banana", "bread")
    meal = ""
    for food in foods:
        meal += food + " "
    return meal[:-1]

# Call the function and print the result
print('Exercise 2:', combine_foods())

# Exercise 3: Slicing Tuples
#
# Using the slice operator, assign a new tuple containing only the last two food strings in the foods to a variable named last_two_foods.

def slice_foods():
    # your code here
    # Create a tuple named foods with at least four food items.
    # Use slicing (example below) to create a new tuple containing only the last two foods.
    # Return that new tuple.
    foods = ("pizza", "taco", "sushi", "steak")
    return foods[-2:]

# Call the function and print the result
print('Exercise 3:', slice_foods())

# Exercise 4: Dictionaries and String Formatting
#
# Create a dictionary named home_town containing the keys of city, state, and population.
# Using the home_town dictionary, assign to a variable named home_town_message a string with this format: “I was born in <city>, <state> - population of <population>”


def hometown_info():
    # your code here
    home_town = {
        "city": "Made Up City",
        "state": "New York",
        "population": 10000
    }
    home_town_message = f"I was born in {home_town['city']}, {home_town['state']} - population of {home_town['population']}"
    return home_town_message

# Call the function and print the result
print('Exercise 4:', hometown_info())

# Exercise 5: Iterating Over Dictionary Items
#
# Define an empty list named home_town_items.
# Use a for loop to iterate over the key: value pairs in the home_town dictionary and append a string with the following format to home_town_items: "<key> = <value>"

# Updated:
# Re-create the home_town dictionary (do not rely on another function).
# Define an empty list named home_town_items.
# Use a for loop to iterate over the dictionary using .items().
# Append strings in this format to the list:
def list_home_town_items():
    # your code here
    home_town = {
        "city": "Made Up City",
        "state": "New York",
        "population": 10000
    }
    home_town_items = []
    for key,val in home_town.items():
        home_town_items.append(f"{key} = {val}")
    return home_town_items

# Call the function and print the result
print('Exercise 5:', list_home_town_items())
