spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    names = []
    for food in spicy_foods:
        names.append(food['name'])
    return names

def get_spiciest_foods(spicy_foods):
    spiciest = []
    for food in spicy_foods:
        if food['heat_level'] > 5:
            spiciest.append(food)
    return spiciest

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        emoji = '🌶' * food['heat_level']
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {emoji}")


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if cuisine == food['cuisine']:
            return food

def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
         if food['heat_level'] > 5:
            emoji = '🌶' * food['heat_level']
            print(f"{food['name']} ({food['cuisine']}) | Heat Level: {emoji}")

def get_average_heat_level(spicy_foods):
    totalheatlvl = 0
    for food in spicy_foods:
        totalheatlvl = food['heat_level'] + totalheatlvl

    spicyfoodsum = len(spicy_foods)
    if spicyfoodsum == 0:
        return 0
    else:
        return totalheatlvl / spicyfoodsum

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
    


### `create_spicy_food()`

# Define a function `create_spicy_food()` that takes a list of `spicy_foods` and a
# new `spicy_food` and returns the original list with the new `spicy_food` added.

# Example:

# ```py
# create_spicy_food(
#     spicy_foods,
#     {
#         'name': 'Griot',
#         'cuisine': 'Haitian',
#         'heat_level': 10,
#     }
# )

# => [
# =>     {
# =>         "name": "Green Curry",
# =>         "cuisine": "Thai",
# =>         "heat_level": 9,
# =>     },
# =>     {
# =>         "name": "Buffalo Wings",
# =>         "cuisine": "American",
# =>         "heat_level": 3,
# =>     },
# =>     {
# =>         "name": "Mapo Tofu",
# =>         "cuisine": "Sichuan",
# =>         "heat_level": 6,
# =>     },
# =>     {
# =>         'name': 'Griot',
# =>         'cuisine': 'Haitian',
# =>         'heat_level': 10,
# =>     },
# => ]


