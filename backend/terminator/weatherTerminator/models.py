from datetime import date
import os
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.contrib import auth
from django.contrib.auth.hashers import make_password


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, nickname, password=None, **extra_fields):
        if not nickname:
            raise ValueError('An email is required.')
        if not password:
            raise ValueError('A password is required.')

        user = self.model(nickname=nickname, password=password, **extra_fields)
        user.save()
        return user

    def create_superuser(self, nickname, password=None, **extra_fields):
        if not nickname:
            raise ValueError('An email is required.')
        if not password:
            raise ValueError('A password is required.')

        return self._create_user(nickname, password, is_superuser=True, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('Email'), null=True, blank=True, unique=False)
    nickname = models.CharField(_('Имя'), max_length=255, null=False, blank=False, unique=True)

    city = models.CharField(_('City'), null=True, blank=True, unique=False)
    country = models.CharField(_('Country'), null=True, blank=True, unique=False)

    is_superuser = models.BooleanField(default=False)

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'nickname'

    objects = UserManager()

    def get_fullname(self):
        return f"{self.nickname[0]}. "

    def __str__(self):
        return f"{self.country[0]}, {self.city[0]}.  "


class Location(models.Model):
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    # name = models.CharField(max_length=100)
    # image = models.BinaryField(null=True)

    def __str__(self):
        return f"{self.country[0]}, {self.city[0]}.  "

    class Meta:
        managed = False
        db_table = 'location'


class Forecast(models.Model):
    date = models.DateField()
    minTem = models.IntegerField()
    maxTem = models.IntegerField()
    averageTem = models.IntegerField()
    atmosphericPressure = models.IntegerField()
    windSpeed = models.IntegerField()
    precipitation = models.IntegerField()
    city = models.ForeignKey(Location, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'forecast weather'


class Past(models.Model):
    date = models.DateField()
    minTem = models.IntegerField()
    maxTem = models.IntegerField()
    averageTem = models.IntegerField()
    atmosphericPressure = models.IntegerField()
    windSpeed = models.IntegerField()
    precipitation = models.IntegerField()
    city = models.ForeignKey(Location, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'statistics for the past years'


class Abnormal(models.Model):
    year = models.IntegerField(max_length=4, unique=True)
    minT = models.OneToOneField(Past, on_delete=models.SET_NULL, null=True, related_name="pastMinT")
    maxT = models.OneToOneField(Past, on_delete=models.SET_NULL, null=True, related_name="pastMaxT")
    maxWS = models.OneToOneField(Past, on_delete=models.SET_NULL, null=True, related_name="pastWS")
    maxP = models.OneToOneField(Past, on_delete=models.SET_NULL, null=True, related_name="pastP")
    city = models.ForeignKey(Location, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'abnormal weather'
