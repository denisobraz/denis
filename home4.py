#"""каждый день в кафе заходит от 5 до 20 покупателей.каждый покупатель берет от 1 до 3 чашек кофе."""
#"""нужно написать функцию,которая будет генерироватьтестовые данные при каждом вызове.

import random
from datetime import date

def cafe_func():
    people = random.randint(5, 20)
    cups = [(random.randint(1, 3)) for i in range(people)]
    return (people, cups)
print(cafe_func())

# К каждой покупке нужно добавить дату и время до минуты (2 щтдельные переменные).
# Время работы кафе с 9 до 20

def time_func():
    time = []
    sales = cafe_func()
    for i in sales:
        hours = random.randint(9, 20)
        minutes = random.randint(0, 59)
        day = str(date.today())
        time.append((hours, minutes, day))
        time.sort()
    return dict(zip(time, sales))

print(time_func())

# Кафе работает 5 дней в неделю.В конце недели надо составить отчет по количеству клиентов и покупок.

def report_func():
    all_people = 0
    all_cups = 0
    for i in range(5):
        all_people += cafe_func()[0]
        all_cups += cafe_func()[0]

print(report_func())