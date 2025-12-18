# x -= 3 => x = x - 3
# 1. not ; 2. and ; 3. or

age = 19
height = 1.75
complex_number = 1j

base = int(input("Enter base: "))
new_height = int(input("Enter new height: "))
area = int((base * new_height) / 2)
print(f"The area of the triangle is {area}")

side_a = int(input("Enter side a: "))
side_b = int(input("Enter side b: "))
side_c = int(input("Enter side c: "))
perimeter = side_a + side_b + side_c
print(f"The sides of the triangle is {perimeter}")

length = int(input("Enter length: "))
width = int(input("Enter width: "))
area = length * width
perimeter_second = 2 * (length + width)

print(f"The perimeter of the triangle is {perimeter_second} and the area of the triangle is {area}")

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
    print(f"x = {x}, y = {value}")
    if value == 0:
        print("👉 y = 0 when x =", x)
