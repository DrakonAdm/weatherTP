from django.contrib.auth import authenticate, get_user_model
from django.core.exceptions import ValidationError
from rest_framework import serializers
from .models import *
# from djoser.serializers import UserCreateSerializer

UserModel = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('nickname',
                  'password',
                  'email',
                  'country',
                  'city',
                  )

    def validate(self, attrs):
        return attrs

    def inner_create(self, validated_data, is_superuser=False):
        user = User.objects.create(nickname=validated_data['nickname'],
                                   password=validated_data['password'],
                                   email=validated_data['email'],
                                   country=validated_data['country'],
                                   city=validated_data['city'],
                                   is_superuser=is_superuser)
        user.set_password(validated_data['password'])
        user.save()

        return user


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'

    def create(self, clean_data):
        user_obj = UserModel.objects.create_user(nickname=clean_data['nickname'], password=clean_data['password'])
        if 'email' in clean_data:
            user_obj.email = clean_data['email']
        if 'country' in clean_data:
            user_obj.country = clean_data['country']
        if 'city' in clean_data:
            user_obj.city = clean_data['city']
        user_obj.save()
        return user_obj


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def check_user(self, clean_data):
        user = authenticate(username=clean_data['email'], password=clean_data['password'])
        if not user:
            raise ValidationError('user not found')
        return user


class ForecastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forecast
        fields = ('id',
                  'date',
                  'minTem',
                  'maxTem',
                  'averageTem',
                  'atmosphericPressure',
                  'windSpeed',
                  'precipitation',
                  'city')


class PastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Past
        fields = ('id',
                  'date',
                  'minTem',
                  'maxTem',
                  'averageTem',
                  'atmosphericPressure',
                  'windSpeed',
                  'precipitation',
                  'city')


class AbnormalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Abnormal
        fields = ('id',
                  'year',
                  'minT',
                  'maxT',
                  'maxWS',
                  'maxP',
                  'city')


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('id', 'country', 'city')
