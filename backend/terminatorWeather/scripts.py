from django.utils import timezone
from datetime import timedelta
from django.utils.datetime_safe import date
import requests

from .models import Forecast, Past, Abnormal, Location


def check_and_move_forecast():
    today = timezone.now().date()

    # фильтр меньше сегодняшней даты
    forecasts = Forecast.objects.filter(date__lt=today)

    for forecast in forecasts:
        past = Past.objects.create(
            date=forecast.date,
            minTem=forecast.minTem,
            maxTem=forecast.maxTem,
            averageTem=forecast.averageTem,
            atmosphericPressure=forecast.atmosphericPressure,
            windSpeed=forecast.windSpeed,
            precipitation=forecast.precipitation,
            city=forecast.city
        )
        past.save()
        forecast.delete()


def update_Abnormal():
    # Get the current year
    current_year = date.today().year
    # Get the previous day's date
    previous_date = timezone.now() - timedelta(days=1)
    try:
        # Get the Past record for the previous day
        past_records = Past.objects.filter(date=previous_date)
    except Past.DoesNotExist:
        return  # No Past record available for the previous day
    # Get all Abnormal records for the current year
    abnormal_records = Abnormal.objects.filter(year=current_year)

    """если ничего не вернула, для первого дня в году (ненормальное 1 января))"""
    if not abnormal_records:
        available_cities = Location.objects.values_list('id', flat=True)

        # Loop through the available cities
        for city in available_cities:
            abnormal_record = Abnormal.objects.create(year=current_year, city=city)
            try:
                past_record = past_records.filter(city=city)
                abnormal_record.minT = past_record
                abnormal_record.maxT = past_record
                abnormal_record.maxWS = past_record
                abnormal_record.maxP = past_record
                abnormal_record.save()
            except Past.DoesNotExist:
                pass
        return

    for abnormal_record in abnormal_records:
        for past_record in past_records:
            if abnormal_record.city == past_record.city:
                if abnormal_record.minT is None or past_record.minTem < abnormal_record.minT.minTem:
                    abnormal_record.minT = past_record

                if abnormal_record.maxT is None or past_record.maxTem > abnormal_record.maxT.maxTem:
                    abnormal_record.maxT = past_record

                if abnormal_record.maxWS is None or past_record.windSpeed > abnormal_record.maxWS.windSpeed:
                    abnormal_record.maxWS = past_record

                if abnormal_record.maxP is None or past_record.atmosphericPressure > abnormal_record.maxP.atmosphericPressure:
                    abnormal_record.maxP = past_record

                # Save the updated Abnormal record
                abnormal_record.save()
                break


def updateForecastWeather(forecast):
    s_city = forecast.city.city
    city_id = 0
    appid = "64c6f0b67e2b86bd96ba6abd37d01ef6"
    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/find",
                           params={'q': s_city, 'type': 'like', 'units': 'metric', 'APPID': appid})
        data = res.json()
        city_id = data['list'][0]['id']

        try:
            res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                               params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
            data = res.json()

            forecast.minTem = data['main']['temp_min']
            forecast.maxTem = data['main']['temp_max']
            forecast.averageTem = data['main']['temp']
            forecast.atmosphericPressure = data['main']['pressure']
            forecast.windSpeed = data['wind']['speed']

            if 'rain' not in data:
                forecast.precipitation = 0
            else:
                forecast.precipitation = data['rain']['1h']

            forecast.save()
        except Exception as e:
            pass

    except Exception as e:
        pass


def updateForecastToday():
    today = timezone.now().date()

    # фильтр сегодняшнюю даты
    forecasts = Forecast.objects.filter(date=today)
    for forecast in forecasts:
        updateForecastWeather(forecast)


def createMonth():
    for i in range(1, 5):
        updateForecastThirtySecondDay(i)


def updateForecastThirtySecondDay(integerDay=4):
    today = timezone.now().date() + timedelta(days=integerDay)
    locations = Location.objects.all()

    # Loop through the available cities
    for location in locations:
        forecast = Forecast.objects.create(date=today, city=location)
        forecastWeatherForSix(forecast)


def forecastWeatherForSix(forecast):
    s_city = forecast.city.city
    appid = "64c6f0b67e2b86bd96ba6abd37d01ef6"

    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                           params={'q': s_city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
        data = res.json()
        forecastDate = forecast.date
        for i in data['list']:
            searchDate = i['dt_txt'].split()[0]

            if str(forecastDate) == str(searchDate):

                if i['dt_txt'].split()[1] == "00:00:00":
                    forecast.minTem = i['main']['temp_min']
                    forecast.save()

                if i['dt_txt'].split()[1] == "12:00:00":
                    forecast.averageTem = i['main']['temp']
                    forecast.save()

                if i['dt_txt'].split()[1] == "12:00:00":
                    forecast.maxTem = i['main']['temp_max']
                    forecast.atmosphericPressure = i['main']['pressure']
                    forecast.windSpeed = i['wind']['speed']
                    forecast.save()
                if 'rain' not in i:
                    forecast.precipitation = 0
                    forecast.save()

                else:
                    forecast.precipitation = i['rain']['3h']
                    forecast.save()

    except Exception as e:
        print("Exception (forecast):", e)
        pass


# def updateForecastWeather(forecast):
#     token = '56b30cb255.3443075'
#     urlID = f'https://api.gismeteo.net/v2/search/cities/?lang=en&query={forecast.city.city}'
#     headers = {
#         'X-Gismeteo-Token': token,
#         'Accept-Encoding': 'gzip, deflate'
#     }
#
#     responseID = requests.get(urlID, headers=headers)
#     print(responseID.json())
#
#     citiesID = None
#     if responseID.status_code == 200:
#         dataID = responseID.json()
#         citiesID = dataID.data.get('id')
#
#
#     url = f'https://api.gismeteo.net/v2/weather/forecast/aggregate/{citiesID}/' \
#           f'{forecast.date.strftime("%Y-%m-%d")}/?lang=ru&days=3'
#
#     response = requests.get(url, headers=headers)
#     if response.status_code == 200:
#         print(response.json())
#         data = response.json()
#         forecast_data = data.get('data', {})
#         for forecast_item in forecast_data:
#             if forecast_item.get('kind') == 'Obs':
#                 temperature = forecast_item.get('temperature', {}).get('air', {})
#                 forecast.minTem = temperature.get('min', {}).get('C')
#                 forecast.maxTem = temperature.get('max', {}).get('C')
#                 forecast.averageTem = temperature.get('avg', {}).get('C')
#                 forecast.atmosphericPressure = forecast_item.get('pressure', {}).get('mm_hg_atm', {}).get('min')
#                 forecast.windSpeed = forecast_item.get('wind', {}).get('speed', {}).get('avg', {}).get('m_s')
#                 forecast.precipitation = forecast_item.get('precipitation', {}).get('amount')
#                 forecast.save()
#                 break


