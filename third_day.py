# \n: new line
# \t: Tab means(8 spaces) or 4 spaces

text = 'It\'s Python'  # Экранирование одинарной кавычки
print(text)  # Вывод: It's Python

quote = "He said: \"Hello!\""
print(quote)  # Вывод: He said: "Hello!"

path = "C:\\Users\\Admin"
print(path)  # Вывод: C:\Users\Admin

challenge = 'thirty days of python'
print(challenge.count('y', 7, 14)) # 1,  mezdu 7 i 14 indexami

challenge = 'thirty\tdays\tof\tpython'
print(challenge.expandtabs())   # 'thirty  days    of      python'
print(challenge.expandtabs(10)) # 'thirty    days      of        python'


print("1. Конкатенация строк")
print(' '.join(['Thirty', 'Days', 'Of', 'Python']))
print(' '.join(['Coding', 'For', 'All']))
print()

print("2. Переменная company")
company = "Coding For All"
print(company)
print(f"Длина строки: {len(company)}")
print(f"Верхний регистр: {company.upper()}")
print(f"Нижний регистр: {company.lower()}")
print(f"Capitalize: {company.capitalize()}")
print(f"Title: {company.title()}")
print(f"Swapcase: {company.swapcase()}")
print(f"Срез первого слова: {company[7:]}")
print()

print("3. Проверка подстроки")
print(f"'Coding' in company: {'Coding' in company}")
print(f"Индекс 'Coding': {company.index('Coding')}")
print(f"Индекс 'Coding' через find: {company.find('Coding')}")
print(f"Замена 'Coding' на 'Python': {company.replace('Coding', 'Python')}")
print(f"Замена 'Everyone' на 'All': {'Python for Everyone'.replace('Everyone', 'All')}")
print()

print("4. Разделение строк")
print(company.split())
print("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(', '))
print()

print("5. Индексы символов")
print(f"Символ на индексе 0: {company[0]}")
print(f"Последний индекс строки: {len(company)-1}")
print(f"Символ на индексе 10: {company[10]}")
print()

print("6. Аббревиатуры")
sentence1 = 'Python For Everyone'
acronym1 = ''.join(word[0] for word in sentence1.split())
print(f"Аббревиатура 'Python For Everyone': {acronym1}")
sentence2 = 'Coding For All'
acronym2 = ''.join(word[0] for word in sentence2.split())
print(f"Аббревиатура 'Coding For All': {acronym2}")
print()

print("7. Индексы символов")
print(f"Индекс 'C': {company.index('C')}")
print(f"Индекс 'F': {company.index('F')}")
print(f"Последний индекс 'l' в 'Coding For All People': {'Coding For All People'.rfind('l')}")
print()

sentence = 'You cannot end a sentence with because because because is a conjunction'
print("8. Работа с 'because'")
print(f"Первое вхождение 'because': {sentence.find('because')}")
print(f"Последнее вхождение 'because': {sentence.rindex('because')}")
print(f"Срез 'because because because': {sentence[31:54]}")
print()

print("9. Проверка начала и конца строки")
print(f"Начинается с 'Coding': {company.startswith('Coding')}")
print(f"Заканчивается на 'coding': {company.endswith('coding')}")
print(f"Удаление пробелов: {'   Coding For All      '.strip()}")
print()

print("10. Проверка идентификатора")
print(f"30DaysOfPython: {'30DaysOfPython'.isidentifier()}")
print(f"thirty_days_of_python: {'thirty_days_of_python'.isidentifier()}")
print()

libs = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print("11. Объединение списка")
print(' # '.join(libs))
print()

print("12. Escape-последовательности")
print("I am enjoying this challenge.\nI just wonder what is next.")
print("Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki")
print()

print("13. Форматирование строк")
radius = 10
area = 3.14 * radius ** 2
print(f"The area of a circle with radius {radius} is {area} meters square.")
a, b = 8, 6
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b:.2f}")
print(f"{a} % {b} = {a % b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} ** {b} = {a ** b}")
