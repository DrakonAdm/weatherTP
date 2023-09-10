import os
from datetime import datetime
from .models import *

file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), './static/pastWeather.txt')
with open(file_path, 'r', encoding='utf-8') as file:
    for line in file:
        # Разбиваем строку на отдельные значения
        values = line.strip().split()

        # Получаем название города и дату из первых двух значений
        if len(values) == 9:
            city_name = values[0] + " " + values[1]
            date_str = values[2]
            i = 1
        else:
            city_name = values[0]
            date_str = values[1]
            i = 0

        # Преобразуем строку даты в объект datetime
        date = datetime.strptime(date_str, '%d.%m.%Y').date()

        # Получаем объект Location для данного города
        location = Location.objects.get(city=city_name)
        if int(values[i + 6]) == (-1000):
            ws = 0
        else:
            ws = int(values[i + 6])

        # Создаем объект Past и сохраняем его в базе данных

        past = Past(date=date,
                    minTem=float(values[i + 2]),
                    maxTem=float(values[i + 3]),
                    averageTem=float(values[i + 4]),
                    atmosphericPressure=float(values[i + 5]),
                    windSpeed=ws,
                    precipitation=float(values[i + 7]),
                    city=location)
        past.save()