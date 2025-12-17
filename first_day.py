"""
terminal -> python --version and На macOS по умолчанию нет команды python, есть python3.\
справа снизу это версия пайтона (interpreter)
"""

print(abs(-7)) # abs() это модуль

print(all([7, 1 ,0])) #фалс скопировать строку это команд + шифт + стрелка вправо (начинай слева)
print(all([7, 1 ,3])) #true

print(any([7, 0 ,0])) #true
print(any([""])) #false

print(ord(" ")) #Возвращает “код” символа (в Unicode; для ASCII это те же числа).
print(ord("A")) #Возвращает “код” символа (в Unicode; для ASCII это те же числа).

print(chr(65)) #A, наоборот

# Важно: это Unicode, поэтому работает и с русскими:

print(bin(5))   # '0b101'
print(bin(10))  # '0b1010'
print(bin(5)[2:])  # '101'

int('101', 2)   # 5 типо двоичное число в обычное 2 и означает это
int('0b101', 2) # 5

s = "hello"
print(dir(s)) # Выдаст список методов строки, типа: upper, lower, split, replace, …

x = "hello"
print(dir()) # показывает элементы какие есть в коде

print(10 == 10.0) #true

# Day 2: 30 Days of python programming

# Exercises: Level 1
first_name = "k1v"
last_name = "k2v"
full_name = first_name + " " + last_name
country = "Estonia"
city = "Valga"
age = 19
year = 2025
is_married = False
is_true = True
is_light_on = True

# Declare multiple variable on one line
a, b, c = 1, 2, 3

# Exercises: Level 2

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

f = len(first_name)
l = len(last_name)
print("len(first_name) =", f)
print("len(last_name)  =", l)
print("Same length?", f == l)

num_one = 5
num_two = 4

total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_one % num_two
exp = num_one ** num_two
floor_division = num_one // num_two

print("total =", total)
print("diff =", diff)
print("product =", product)
print("division =", division)
print("remainder =", remainder)
print("exp =", exp)
print("floor_division =", floor_division)

r = 30
pi = 3.14
area_of_circle = pi * r ** 2
circum_of_circle = 2 * pi * r
print("area_of_circle =", area_of_circle)
print("circum_of_circle =", circum_of_circle)

r = float(input("Enter radius: "))
area_circle = pi * r ** 2
circumference = 2 * pi * r
print("area_circle =", area_circle)
print("circumference =", circumference)

first_name = input("First name: ")
last_name = input("Last name: ")
country = input("Country: ")
age = input("Age: ")

print("You entered:", first_name, last_name, country, age)

help("keywords")
