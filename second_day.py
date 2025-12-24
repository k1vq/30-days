# x -= 3 => x = x - 3
# 1. not ; 2. and ; 3. or

age = 19
height = 1.75
complex_number = 1j

base = int(input("Enter base: "))
new_height = int(input("Enter new height: "))
area = 0.5 * base * new_height
print(f"The area of the triangle is {area}")

side_a = int(input("Enter side a: "))
side_b = int(input("Enter side b: "))
side_c = int(input("Enter side c: "))
perimeter = side_a + side_b + side_c
print(f"The perimeter of the triangle is {perimeter}")

length = int(input("Enter length: "))
width = int(input("Enter width: "))
area = length * width
perimeter_second = 2 * (length + width)

print(f"The perimeter of the rectangle is {perimeter_second} and the area of the rectangle is {area}")

r = float(input("Enter radius: "))
pi = 3.14
circumference = 2 * pi * r
area_of_circle = pi * r * r
print(f"The area of the circle is {area_of_circle} and the circumference is {circumference}")

# equation: y = 2x - 2

m = 2              # slope
y_intercept = -2   # when x = 0
x_intercept = 1    # when y = 0

print("Slope:", m)
print("x-intercept:", (x_intercept, 0))
print("y-intercept:", (0, y_intercept))

import math

# given points
x1, y1 = 2, 2
x2, y2 = 6, 10

# slope
m_first = (y2 - y1) / (x2 - x1)

# Euclidean distance
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2) # sqrt - квадратный корень ( import math )

print("Slope:", m_first)
print("Euclidean distance:", distance)
print(m_first == m)

def y(x):
    return x**2 + 6*x + 9

for x in range(-10, 11):
    value = y(x)
    print(f"x = {x}, y = {value}") # Выводим пары (x, y) и проверяем, при каком x значение функции равно нулю
    if value == 0:
        print("👉 y = 0 when x =", x) # Перебираем x от -10 до 10, вычисляем y = x^2 + 6x + 9 для каждого значения

python = len("python")
dragon = len("dragon")

print(python != dragon)

print("on" in ("python" and "dragon")) # skobki postavit' ewe # print("on" in "python" and "on" in "dragon")

print("jargon" in "I hope this course is not full of jargon")

print("on" not in ("python" and "dragon")) # print("on" not in "python" and "on" not in "dragon")

float_python = float(len("python"))

print(str(float_python))

number = 10

if number % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

print((7 // 3) == int(2.7))

print(type("10") == type(10))

print(int("9.8") == 10)

hours = int(input("Enter hours: "))
per_hour = int(input("Enter rate per hour: "))

print(f"Your weekly earning is {hours * per_hour}")

years = int(input("Enter number of years: "))
print(f"You have lived for {years * 31536000} seconds")

for i in range(1, 6):
    print(i, 1, i**2, i**3)

    """
    i = 1 → 1 1 1 1 1

    i = 2 → 2 1 2 4 8

    i = 3 → 3 1 3 9 27

    i = 4 → 4 1 4 16 64

    i = 5 → 5 1 5 25 125
    """
