# syntax
lst = list()

# syntax
lst_1 = []

lst_2 = ['Asabeneh', 250, True, {'country': 'Finland', 'city': 'Helsinki'}]  # list containing different data types

lst_3 = ['item1','item2','item3', 'item4', 'item5']
first_item, second_item, third_item, *rest = lst_3
print(first_item)     # item1
print(second_item)    # item2
print(third_item)     # item3
print(rest)           # ['item4', 'item5']

# copy() — создать копию списка
lst_4 = [1, 2, 3]
lst_copy = lst_4.copy()
lst_4.append(4)
print(lst_4)       # [1, 2, 3]
print(lst_copy)  # [1, 2, 3, 4]

# Level 1
empty_list = []

list_items = [1, 2, 3, 4, 5, 6]

print(len(list_items))

print(list_items[0], list_items[len(list_items)//2], list_items[-1])

mixed_data_types = ['Name', 25, 1.75, 'Single', 'Address']

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

print(it_companies)
print(len(it_companies))
print(it_companies[0], it_companies[len(it_companies)//2], it_companies[-1])

it_companies[0] = 'Meta'
print(it_companies)

it_companies.append('Twitter')
it_companies.insert(len(it_companies)//2, 'Netflix')
it_companies[1] = it_companies[1].upper()

print('#;  '.join(it_companies))
print('Google' in it_companies)

it_companies.sort()
print(it_companies)

it_companies.reverse()
print(it_companies)

print(it_companies[:3])
print(it_companies[-3:])

middle = len(it_companies)//2
if len(it_companies)%2 == 0:
    print(it_companies[middle-1:middle+1])
else:
    print(it_companies[middle])

it_companies.pop(0)

middle = len(it_companies)//2
if len(it_companies)%2 == 0:
    del it_companies[middle-1:middle+1]
else:
    del it_companies[middle]

it_companies.pop(-1)
it_companies.clear()
del it_companies

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end  = ['Node', 'Express', 'MongoDB']

full_stack = front_end + back_end
full_stack_copy = full_stack.copy()
idx = full_stack_copy.index('Redux')
full_stack_copy.insert(idx+1, 'Python')
full_stack_copy.insert(idx+2, 'SQL')


# Level 2
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages.sort()
print(min(ages), max(ages))

ages.append(min(ages))
ages.append(max(ages))

middle = len(ages)//2
if len(ages)%2 == 0:
    median = (ages[middle-1] + ages[middle]) / 2
else:
    median = ages[middle]
print(median)

average = sum(ages)/len(ages)
print(average)

print(max(ages) - min(ages))
print(abs(min(ages)-average), abs(max(ages)-average))

countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']

middle = len(countries)//2
if len(countries)%2 == 0:
    print(countries[middle-1:middle+1])
else:
    print(countries[middle])

half = len(countries)//2
if len(countries)%2 == 0:
    first_half  = countries[:half]
    second_half = countries[half:]
else:
    first_half  = countries[:half+1]
    second_half = countries[half+1:]

first_three, *scandic_countries = countries[:3], countries[3:]
print(first_three, scandic_countries)
