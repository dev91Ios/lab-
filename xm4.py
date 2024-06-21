import random as r

answers = ['Норм.', 'Лучше всех :)', 'Ну так', 'Отличненько!', 'Ничего, жить буду']

def how_are_you(answer):
    return (r.choice(answer))


print(how_are_you(['Норм.', 'Лучше всех :)', 'Ничего, жить буду']))
