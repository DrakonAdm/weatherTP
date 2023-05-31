from datetime import date

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


# class MyUserManager(BaseUserManager):
#
#     def _create_user(self, nickname, email, password, **extra_fields):
#         if len(password) < 8:
#             raise ValueError('Минимальная длина пароля 8 символов')
#         elif len(nickname) < 4:
#             raise ValueError('Минимальная длина никнейма 4 символов')
#
#         user = User(
#             nickname=nickname,
#             email=email,
#             **extra_fields
#         )
#
#         user.set_password(password)
#         user.save()
#         return user
#
#     def create_user(self, nickname, email, password):
#         return self._create_user(nickname, email, password)
#
#     def create_superuser(self, nickname, email, password):
#         return self._create_user(nickname, email, password, is_staff=True, is_superuser=True)
#
#
# class User(AbstractBaseUser, PermissionsMixin):
#     id = models.AutoField(primary_key=True, unique=True)
#     nickname = models.CharField(max_length=100, unique=True)
#     email = models.CharField()
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     is_superuser = models.BooleanField(default=False)
#
#     USERNAME_FIELD = 'nickname'
#
#     objects = MyUserManager()
#
#     def __str__(self):
#         return self.nickname


class Location(models.Model):
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    # name = models.CharField(max_length=100)
    # image = models.BinaryField(null=True)

    def __str__(self):
        return self.city

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
    minT = models.OneToOneField(Past, on_delete=models.SET_NULL, null=True, related_name="pastMinT")
    maxT = models.OneToOneField(Past, on_delete=models.SET_NULL, null=True, related_name="pastMaxT")
    maxWS = models.OneToOneField(Past, on_delete=models.SET_NULL, null=True, related_name="pastWS")
    maxP = models.OneToOneField(Past, on_delete=models.SET_NULL, null=True, related_name="pastP")
    city = models.ForeignKey(Location, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'abnormal weather'
