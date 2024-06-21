# лаба номер 8
# ЗАДАНИЕ 1
import random

def catch_ball():
    return random.random() < 0.7

def computer_response():
    responses = ["Я думаю, что...", "Это секрет!", "Не могу сказать"]
    return random.choice(responses)

def player_response():
    return input("Ваш ответ на вопрос: ")

# История ходов
history = []

for _ in range(10):
    print("Ход", len(history) + 1)
    print("Компьютер бросает вам мяч...")
    if catch_ball():
        print("Вы поймали мяч!")
        question = "Какой ваш любимый цвет?"
        answer = player_response()
    else:
        print("Вы не поймали мяч.")
        question = "Какой ваш любимый фильм?"
        answer = computer_response()
    
    history.append(("Вы", question, answer))

    print("Вы бросаете мяч компьютеру...")
    if catch_ball():
        print("Компьютер поймал мяч!")
        question = "Какой ваш любимый вид спорта?"
        answer = computer_response()
    else:
        print("Компьютер не поймал мяч.")
        question = "Какое ваше любимое блюдо?"
        answer = input("Ответ компьютера: ")
    
    history.append(("Компьютер", question, answer))

# Вывод истории
print("\nИстория:")
for turn in history:
    print(turn)


# ЗАДАНИЕ 2
def reverse_number(number):
    return int(str(number)[::-1])

def is_palindrome(number):
    return str(number) == str(number)[::-1]

def process_numbers(numbers):
    reversed_numbers = []
    for num in numbers:
        reversed_num = reverse_number(num)
        if is_palindrome(num):
            print(f"Число {num} является палиндромом.")
        reversed_numbers.append(reversed_num)
    return reversed_numbers

# Пример использования функций
numbers = [123, 555, 987, 121, 456]
reversed_list = process_numbers(numbers)
print("Новый список с перевернутыми числами:", reversed_list)


# ЗАДАНИЕ 3
def compound_interest(principal, rate, years):
    amount = principal * (1 + rate)**years
    return amount

principal = float(input("Введите начальную сумму: "))
rate = float(input("Введите процентную ставку (в виде десятичной дроби): "))
years = int(input("Введите количество лет: "))

result = compound_interest(principal, rate, years)
print(f"Через {years} лет ваша инвестиция вырастет до: {result:.2f}")


# ЗАДАНИЕ 4
import random

def generate_doors(num_doors, num_prizes):
    doors = ["пусто"] * num_doors
    prize_indices = random.sample(range(num_doors), num_prizes)
    for idx in prize_indices:
        doors[idx] = "приз"
    return doors

def simulate_game(num_doors, num_prizes):
    doors = generate_doors(num_doors, num_prizes)
    
    player1_choice = random.randint(0, num_doors - 1)
    player2_choice = random.randint(0, num_doors - 1)
    
    opened_door = random.choice([idx for idx, door in enumerate(doors) if door == "пусто" and idx != player1_choice])
    
    if doors[player1_choice] == "приз":
        player1_wins_no_change = 1
    else:
        player1_wins_no_change = 0
        
    if doors[player2_choice] == "приз":
        player2_wins_no_change = 1
    else:
        player2_wins_no_change = 0
        
    if doors[player2_choice] == "приз":
        player2_wins_change = 0
    else:
        player2_wins_change = 1
        
    return player1_wins_no_change, player2_wins_no_change, player2_wins_change

num_doors = int(input("Введите количество дверей: "))
num_prizes = int(input("Введите количество призов: "))

num_simulations = 10000
total_player1_wins_no_change = 0
total_player2_wins_no_change = 0
total_player2_wins_change = 0

for _ in range(num_simulations):
    p1, p2_no_change, p2_change = simulate_game(num_doors, num_prizes)
    total_player1_wins_no_change += p1
    total_player2_wins_no_change += p2_no_change
    total_player2_wins_change += p2_change

prob_player1_no_change = total_player1_wins_no_change / num_simulations
prob_player2_no_change = total_player2_wins_no_change / num_simulations
prob_player2_change = total_player2_wins_change / num_simulations

print(f"Вероятность выигрыша для игрока, оставшегося при своем первоначальном выборе: {prob_player1_no_change:.4f}")
print(f"Вероятность выигрыша для игрока, не меняющего свой выбор: {prob_player2_no_change:.4f}")
print(f"Вероятность выигрыша для игрока, меняющего свой выбор: {prob_player2_change:.4f}")


# ЗАДАНИЕ 5
import random

# Списки предметов разных редкостей
common_items = ["Обычный предмет 1", "Обычный предмет 2", "Обычный предмет 3"]
rare_items = ["Редкий предмет 1", "Редкий предмет 2"]
epic_items = ["Эпический предмет 1", "Эпический предмет 2"]
legendary_items = ["Легендарный предмет 1"]

# Шансы на выпадение предметов
chances = {
    "common": 0.7,
    "rare": 0.2,
    "epic": 0.1,
    "legendary": 0.05
}

# Счетчики выпавших предметов
counts = {
    "common": 0,
    "rare": 0,
    "epic": 0,
    "legendary": 0
}

# Открытие лутбоксов
lootbox_count = 20
items = []

for _ in range(lootbox_count):
    rand = random.random()
    if rand < chances["common"]:
        item = random.choice(common_items)
        counts["common"] += 1
    elif rand < chances["common"] + chances["rare"]:
        item = random.choice(rare_items)
        counts["rare"] += 1
    elif rand < chances["common"] + chances["rare"] + chances["epic"]:
        item = random.choice(epic_items)
        counts["epic"] += 1
    else:
        item = random.choice(legendary_items)
        counts["legendary"] += 1
    items.append(item)

# Проверка условий
luck_message = ""
if counts["epic"] > 3:
    luck_message = " (Удача!)"
if counts["legendary"] > 1:
    luck_message = " (Большая удача!)"

# Вывод результатов
print(f"Обычные предметы: {counts['common']}")
print(f"Редкие предметы: {counts['rare']}")
print(f"Эпические предметы: {counts['epic']}")
print(f"Легендарные предметы: {counts['legendary']}")
print(luck_message)

# Отображение полученных предметов разного цвета
for item in items:
    if item in common_items:
        print(f"\033[0m{item}")  # белый цвет
    elif item in rare_items:
        print(f"\033[34m{item}")  # синий цвет
    elif item in epic_items:
        print(f"\033[35m{item}")  # фиолетовый цвет
    else:
        print(f"\033[33m{item}")  # оранжевый цвет