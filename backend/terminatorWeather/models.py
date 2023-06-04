from django.contrib.auth.hashers import make_password
from django.core.validators import MinValueValidator
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils.translation import gettext_lazy as _


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
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    # name = models.CharField(max_length=100)
    # image = models.BinaryField(null=True)

    def __str__(self):
        return f"{self.country[0]}, {self.city[0]}.  "

    class Meta:
        managed = True
        db_table = 'location'


class Forecast(models.Model):
    date = models.DateField()
    minTem = models.IntegerField()
    maxTem = models.IntegerField()
    averageTem = models.IntegerField()
    atmosphericPressure = models.IntegerField(validators=[MinValueValidator(0)])
    windSpeed = models.IntegerField(validators=[MinValueValidator(0)])
    precipitation = models.DecimalField(validators=[MinValueValidator(0)], max_digits=5, decimal_places=2)
    city = models.ForeignKey(Location, on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = 'forecast'


class Past(models.Model):
    date = models.DateField()
    minTem = models.IntegerField()
    maxTem = models.IntegerField()
    averageTem = models.IntegerField()
    atmosphericPressure = models.IntegerField(validators=[MinValueValidator(0)])
    windSpeed = models.IntegerField(validators=[MinValueValidator(0)])
    precipitation = models.DecimalField(validators=[MinValueValidator(0)], max_digits=5, decimal_places=2)
    city = models.ForeignKey(Location, on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = 'past'


class Abnormal(models.Model):
    year = models.IntegerField(unique=True)
    minT = models.OneToOneField(Past, on_delete=models.SET_NULL, null=True, related_name="pastMinT")
    maxT = models.OneToOneField(Past, on_delete=models.SET_NULL, null=True, related_name="pastMaxT")
    maxWS = models.OneToOneField(Past, on_delete=models.SET_NULL, null=True, related_name="pastWS")
    maxP = models.OneToOneField(Past, on_delete=models.SET_NULL, null=True, related_name="pastP")
    city = models.ForeignKey(Location, on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = 'abnormal'
