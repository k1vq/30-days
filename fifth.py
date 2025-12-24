# чтобы меня тупл нужно его перевести в лист, поменять что все нужно и перевести в tuple()
# joining tuples = +++++
#deleting tuple ====== del tuple
"""LEVEL 1"""

empty_tuple = tuple()
print(empty_tuple)
brother_and_sister = ("kristina", "ilja")
print(brother_and_sister)
brothers = ("ilja",) # , eto nado esli tok 1 element
sisters = ("kristina",) # , eto nado esli tok 1 element
siblings = brothers + sisters
parents = ("larissa", "vova")
sibling_parents = parents + sisters + brothers
print(sibling_parents)

"""LEVEL 2"""

mother, father, *siblings_unpacked = sibling_parents

print("Mother:", mother)   # larissa
print("Father:", father)   # vova
print("Siblings:", siblings_unpacked)  # ['ilja', 'kristina']

fruits = ("apple", "banana", "orange")
vegetables = ("carrot", "tomato", "cucumber")
animal_products = ("milk", "egg", "cheese")

food_stuff_tp = fruits + vegetables + animal_products
food_stuff_lt = list(food_stuff_tp)

middle_index = len(food_stuff_lt) // 2
middle_items = food_stuff_lt[middle_index-1:middle_index+1] if len(food_stuff_lt) % 2 == 0 else food_stuff_lt[middle_index]

first_three = food_stuff_lt[:3]
last_three = food_stuff_lt[-3:]

del food_stuff_tp

nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)
