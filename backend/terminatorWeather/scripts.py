from django.utils import timezone
from django.utils.datetime_safe import date
# import requests

from .models import Forecast, Past


def check_and_move_forecast():
    # today = timezone.now().date()
    # forecasts = Forecast.objects.filter(date__lt=today)
    #
    # for forecast in forecasts:
    #     past = Past.objects.create(
    #         date=forecast.date,
    #         minTem=forecast.minTem,
    #         maxTem=forecast.maxTem,
    #         averageTem=forecast.averageTem,
    #         atmosphericPressure=forecast.atmosphericPressure,
    #         windSpeed=forecast.windSpeed,
    #         precipitation=forecast.precipitation,
    #         city=forecast.city
    #     )
    #     past.save()
    #     forecast.delete()
    return


def updateForecastWeather():
    return


def get_weather_forecast():
    # """что-то доделать скрипт не доконца верен"""
    # # Получаем список городов из модели Location
    # locations = Location.objects.all()
    #
    # # Получаем текущую дату
    # today = timezone.now().date()
    #
    # for location in locations:
    #     # Формируем URL для запроса прогноза погоды
    #     url = f"https://api.weather.com/v3/wx/forecast/daily/5day?apiKey=<API_KEY>&geocode={location.latitude}," \
    #           f"{location.longitude}&format=json&units=m"
    #
    #     # Отправляем запрос на API
    #     response = requests.get(url)
    #
    #     # Проверяем успешность запроса
    #     if response.status_code == 200:
    #         # Получаем данные о погоде из ответа API
    #         data = response.json()
    #
    #         # Обрабатываем данные и сохраняем прогнозы погоды в модель Forecast
    #         for forecast in data['daypart'][0]['temperature']:
    #             date_str = forecast['validTime'][0:10]
    #             forecast_date = date.fromisoformat(date_str)
    #
    #             if forecast_date >= today:
    #                 min_tem = forecast['minTemp']
    #                 max_tem = forecast['maxTemp']
    #                 avg_tem = forecast['temperature']
    #                 pressure = forecast['pressureSurfaceLevel']
    #                 wind_speed = forecast['windSpeed']
    #                 precipitation = forecast['qpf']
    #
    #                 # Создаем объект модели Forecast и сохраняем его в базу данных
    #                 Forecast.objects.create(
    #                     date=forecast_date,
    #                     minTem=min_tem,
    #                     maxTem=max_tem,
    #                     averageTem=avg_tem,
    #                     atmosphericPressure=pressure,
    #                     windSpeed=wind_speed,
    #                     precipitation=precipitation,
    #                     city=location
    #                 )
    return


"""Нужен скрипт обновления погоды на день, когда он наступил"""
"""Обновление аномальной погоды/ и добавление в неё"""