# 1- Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# *Пример:*

# - 6 -> да
# - 7 -> да
# - 1 -> нет


def week(number):
    if numberday > 7 or numberday < 1:
        return "Не день недели!"
    if numberday > 5 and numberday < 8:
        return "Выходной день!"
    if numberday > 0 and numberday < 6:
        return "Будний день!"
  

numberday = int(input("Введите день недели:"))

print(week(numberday))