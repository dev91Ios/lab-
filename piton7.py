# лаба номер 7
# задание 1
number = int(input("Введите целое число: "))

if number % 2 == 0:
    print(f"Число {number} является четным.")
else:
    print(f"Число {number} является нечетным.")
    
    
    
# задание 2
num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
num3 = float(input("Введите третье число: "))

max_number = num1

if num2 > max_number:
    max_number = num2

if num3 > max_number:
    max_number = num3

print(f"Максимальное число: {max_number}")



# задание 3
number = int(input("Введите целое неотрицательное число: "))

factorial = 1

if number < 0:
    print("Факториал отрицательного числа не определен.")
elif number == 0:
    print("Факториал 0 равен 1.")
else:
    for i in range(1, number + 1):
        factorial *= i
    print(f"Факториал числа {number} равен {factorial}.")



# задание 4
number = int(input("Введите целое число больше 1: "))

if number <= 1:
    print("Число должно быть больше 1.")
else:
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break

    if is_prime:
        print(f"Число {number} является простым.")
    else:
        print(f"Число {number} не является простым.")



# задание 5
number = int(input("Введите число для таблицы умножения: "))

print(f"Таблица умножения для числа {number}:")
for i in range(1, 11):
    result = number * i
    print(f"{number} * {i} = {result}")



# задание 6
def is_palindrome(input_string):
    clean_string = ''.join(char for char in input_string if char.isalnum()).lower()
    return clean_string == clean_string[::-1]

user_input = input("Введите строку для проверки на палиндром: ")

if is_palindrome(user_input):
    print("Введенная строка является палиндромом.")
else:
    print("Введенная строка не является палиндромом.")



# задание 7
def count_vowels_consonants(input_string):
    vowels = 'aeiouAEIOU'
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    
    vowels_count = sum(1 for char in input_string if char in vowels)
    consonants_count = sum(1 for char in input_string if char in consonants)
    
    return vowels_count, consonants_count

user_input = input("Введите строку для подсчета гласных и согласных букв: ")

vowels, consonants = count_vowels_consonants(user_input)

print(f"Количество гласных букв: {vowels}")
print(f"Количество согласных букв: {consonants}")



# задание 8
numbers = [5, 10, 15, 20, 25]

sum_of_numbers = sum(numbers)

print(f"Список чисел: {numbers}")
print(f"Сумма всех элементов списка: {sum_of_numbers}")



# задание 9
n = int(input("Введите натуральное число n: "))

if n <= 0:
    print("Введите натуральное число больше 0.")
else:
    for i in range(n, 0, -1):
        print(i)



# задание 10
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)