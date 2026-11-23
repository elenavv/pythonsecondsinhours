'''
Задание 1
Пользователь вводит с клавиатуры время в секундах, прошедшее с начала дня.
В зависимости от выбора пользователя посчитать, сколько часов, минут и секунд
осталось до полуночи.
1 час = 60*60 = 3600сек
2 часа = 7200 сек
'''
import math #подключение библиотеки
seconds_in_a_day2 = 24*60*60
seconds2 = 7200 # это 1 час 10 минута 10 секунда  до конца дня 22 часа 50 мин 50 сек
hours  = (seconds_in_a_day2-seconds2)//60//60 #часов до конца дня
print(f"Часы {hours}")
minutes = math.ceil((((seconds_in_a_day2-seconds2)/60/60)-hours)*60)
#hours2 = (seconds_in_a_day2-seconds2)//3600
print(f"Минуты {minutes}")
seconds_left = (seconds_in_a_day2-seconds2)%60%60
print(f"Cекунды {seconds_left}")




seconds_in_a_day = 24*60*60
print(f"Секунд в дне {seconds_in_a_day}")
seconds = int(input("Введите время в секундах прошедшее сначала дня: "))
seconds_end_day = seconds_in_a_day - seconds #сколько секунд до конца дня 
minutes_end_day = seconds_end_day/60 #сколько минут до конца дня
hours_end_day = minutes_end_day/60 #сколько часов до конца дня
print(f"До конца дня осталось {hours_end_day} часов\n"
      f"или {minutes_end_day} минут\n"
      f"или {seconds_end_day} секунд ")
