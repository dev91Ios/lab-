# лаба номер 6
# город возраст имя
name = "Дмитрий"
age = 18
city = "Москва"

print("Меня зовут", name)
print("Мой возраст", age, "лет")
print("Я живу в городе", city)


# номер 2 числа
num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))

sum_result = num1 + num2
multiply_result = num1 * num2

print("Сумма чисел:", sum_result)
print("Произведение чисел:", multiply_result)


#любимый цвет
favorite_color = "синий"
print(f"Мой любимый цвет: {favorite_color}")


#настроение
mood = input("Какое у вас сегодня настроение? ")
print(f"Сегодня я чувствую себя {mood}") 


#любимая строка
user_input = input("Введите любую строку: ")
length = len(user_input)
print(f"Длина введенной строки: {length}")


#любимое число
favorite_number = 7
print(f"Моё любимое число: {favorite_number}")


#температура
celsius = float(input("Введите температуру в градусах Цельсия: "))
print(f"Температура в градусах Цельсия: {celsius}")

fahrenheit = (celsius * 9/5) + 32
print(f"Температура в градусах Фаренгейта: {fahrenheit}")



#слово 3 раза
word = input("Введите любое слово: ")
print(f"{word} {word} {word}")



#переменная
my_name = "Peremennay"
upper_case_name = my_name.upper()
lower_case_name = my_name.lower()

print(f"Мое имя в верхнем регистре: {upper_case_name}")
print(f"Мое имя в нижнем регистре: {lower_case_name}")



#число в виде строки
number_str = input("Введите любое число: ")
number_int = int(number_str)
print(f"Введенное число в целочисленном формате: {number_int}")