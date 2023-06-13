import os

from django.contrib.auth.hashers import make_password
from django.core.validators import MinValueValidator
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db.models import Max, Min
from django.utils.translation import gettext_lazy as _
from datetime import datetime


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('An email is required.')
        if not password:
            raise ValueError('A password is required.')

        user = self.model(email=email, password=password, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('Email'), null=False, blank=False, unique=True)
    nickname = models.CharField(_('Имя'), null=True, blank=True, unique=False)

    city = models.CharField(_('City'), max_length=100, null=True, blank=True, unique=False)
    country = models.CharField(_('Country'), max_length=100, null=True, blank=True, unique=False)

    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'

    objects = UserManager()

    def get_fullname(self):
        return f"{self.nickname[0]}. "

    def __str__(self):
        return f"{self.email}."


class Location(models.Model):
    country = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.country}, {self.city}."

    def collectModelLocation(self):
        # Открываем файл с данными
        file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), './static/listLocation.txt')
        with open(file_path, 'r') as f:
            # Читаем строки из файла
            lines = f.readlines()
            for line in lines:
                # Обрабатываем строку и создаем новый объект модели Location
                country, city = line.strip().split(' ', maxsplit=1)
                location = Location.objects.create(country=country, city=city)
                location.save()

    class Meta:
        managed = True
        db_table = 'location'


class Forecast(models.Model):
    date = models.DateField()
    minTem = models.FloatField(null=True)
    maxTem = models.FloatField(null=True)
    averageTem = models.FloatField(null=True)
    atmosphericPressure = models.IntegerField(validators=[MinValueValidator(0)], null=True)
    windSpeed = models.IntegerField(validators=[MinValueValidator(0)], null=True)
    precipitation = models.DecimalField(validators=[MinValueValidator(0)], max_digits=5, decimal_places=2, null=True)
    city = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.date}"

    class Meta:
        managed = True
        db_table = 'forecast'


class Past(models.Model):
    date = models.DateField()
    minTem = models.FloatField()
    maxTem = models.FloatField()
    averageTem = models.FloatField()
    atmosphericPressure = models.FloatField(validators=[MinValueValidator(0)])
    windSpeed = models.IntegerField(validators=[MinValueValidator(0)])
    precipitation = models.DecimalField(validators=[MinValueValidator(0)], max_digits=5, decimal_places=2)
    city = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.date}"

    def read_past_weather_file(self):
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

                # Создаем объект Past и сохраняем его в базе данных
                past = Past(date=date,
                            minTem=float(values[i + 2]),
                            maxTem=float(values[i + 3]),
                            averageTem=float(values[i + 4]),
                            atmosphericPressure=float(values[i + 5]),
                            windSpeed=int(values[i + 6]),
                            precipitation=float(values[i + 7]),
                            city=location)
                past.save()

    class Meta:
        managed = True
        db_table = 'past'


class Abnormal(models.Model):
    year = models.IntegerField()
    minT = models.OneToOneField(Past, on_delete=models.SET_NULL, null=True, related_name="pastMinT")
    maxT = models.OneToOneField(Past, on_delete=models.SET_NULL, null=True, related_name="pastMaxT")
    maxWS = models.OneToOneField(Past, on_delete=models.SET_NULL, null=True, related_name="pastWS")
    maxP = models.OneToOneField(Past, on_delete=models.SET_NULL, null=True, related_name="pastP")
    city = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.year}"

    @staticmethod
    def find_abnormal_weather(start_year=2020, end_year=2023):
        locations = Location.objects.all()

        for location in locations:
            abnormal_weather = []

            past_data = Past.objects.filter(city=location)

            for year in range(start_year, end_year + 1):
                year_data = past_data.filter(date__year=year)

                if year_data:
                    min_tem = year_data.aggregate(Min('minTem'))['minTem__min']
                    max_tem = year_data.aggregate(Max('maxTem'))['maxTem__max']
                    max_ws = year_data.aggregate(Max('windSpeed'))['windSpeed__max']
                    max_p = year_data.aggregate(Max('precipitation'))['precipitation__max']

                    abnormal_year = Abnormal(year=year, city=location)

                    for past in year_data:
                        if past.minTem == min_tem:
                            abnormal_year.minT = past

                        if past.maxTem == max_tem:
                            abnormal_year.maxT = past

                        if past.windSpeed == max_ws:
                            abnormal_year.maxWS = past

                        if past.precipitation == max_p:
                            abnormal_year.maxP = past

                    if abnormal_year.minT or abnormal_year.maxT or abnormal_year.maxWS or abnormal_year.maxP:
                        abnormal_weather.append(abnormal_year)

            Abnormal.objects.bulk_create(abnormal_weather)

    class Meta:
        managed = True
        db_table = 'abnormal'


class Advertisement(models.Model):
    short = models.CharField(_('English'), max_length=20, null=False, blank=False, unique=True)
    long = models.CharField(_('Russian'), max_length=100, null=False, blank=False, unique=False)
    page = models.ImageField()

    def __str__(self):
        return f"{self.short} and {self.long}."

    class Meta:
        managed = True
        db_table = 'advertisement'
