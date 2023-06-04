from django.contrib.auth import logout, login, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.http import request, HttpResponseNotFound, HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from django.utils import timezone
from django.utils.datetime_safe import datetime
from datetime import timedelta

from rest_framework.authentication import SessionAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .models import *
from .serializers import *
from rest_framework import status, generics, viewsets, permissions

from .validations import *


class MyAPIListPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 10000


class ForecastDayAPIView(generics.ListAPIView):
    queryset = Forecast.objects.all()
    serializer_class = ForecastSerializer

    def get_queryset(self):
        city = 'Воронеж'
        country = 'Россия'

        """Если пользователь зареган и у него есть страна/город взять от него """
        if self.request.user.is_authenticated:
            modelUser = get_user_model()
            user = modelUser.objects.get(pk=self.request.user.pk)
            if user.city:
                city = user.city
            if user.country:
                country = user.country

        if 'city' in self.request.GET:
            city = self.request.GET['city']
        if 'country' in self.request.GET:
            country = self.request.GET['country']

        if 'date' in self.request.GET:
            dateSearch = self.request.GET.get('date')
        elif 'tomorrow' in self.request.GET:
            dateSearch = self.request.GET.get('tomorrow')
        else:
            dateSearch = timezone.now().date()

        try:
            dateSearch = datetime.datetime.strptime(dateSearch, '%Y-%m-%d').date()
        except ValueError:
            return Response({'error': 'Invalid date format. Use YYYY-MM-DD.'}, status=status.HTTP_400_BAD_REQUEST)

        queryset = self.queryset.objects.filter(date=dateSearch, city__city=city, city__country=country)

        """вызов скрипта для предсказания одежды"""

        """правильно ли возвращать queryset????"""
        # queryset = self.queryset.objects.filter(date=date)
        # serializer = self.serializer_class(queryset, many=True)
        # return Response(serializer.data)

        return queryset


class ForecastManyDayAPIView(generics.ListAPIView):
    queryset = Forecast.objects.all()
    serializer_class = ForecastSerializer

    pagination_class = MyAPIListPagination

    def get_queryset(self):
        city = 'Воронеж'
        country = 'Россия'

        """Если пользователь зареган и у него есть страна/город взять от него """
        if self.request.user.is_authenticated:
            modelUser = get_user_model()
            user = modelUser.objects.get(pk=self.request.user.pk)
            if user.city:
                city = user.city
            if user.country:
                country = user.country

        if 'city' in self.request.GET:
            city = self.request.GET['city']
        if 'country' in self.request.GET:
            country = self.request.GET['country']

        queryset = self.queryset.objects.filter(city__city=city, city__country=country)
        if 'days' in self.request.GET:
            queryset = queryset.objects.filter(date__lte=timezone.now().date() + timedelta(days=9))

        return queryset


class PastView(generics.ListAPIView):
    queryset = Past.objects.all()
    serializer_class = PastSerializer

    permission_classes = [IsAuthenticated]

    pagination_class = MyAPIListPagination

    def get_queryset(self):
        city = 'Воронеж'
        country = 'Россия'

        """Если пользователь зареган и у него есть страна/город взять от него """
        if self.request.user.is_authenticated:
            modelUser = get_user_model()
            user = modelUser.objects.get(pk=self.request.user.pk)
            if user.city:
                city = user.city
            if user.country:
                country = user.country

        if 'city' in self.request.GET:
            city = self.request.GET['city']
        if 'country' in self.request.GET:
            country = self.request.GET['country']

        queryset = self.queryset.objects.filter(city__city=city, city__country=country)

        if 'firstDate' in self.request.GET and 'secondDate' in self.request.GET:
            firstDate = self.request.GET.get('firstDate')
            secondDate = self.request.GET.get('secondDate')
            try:
                firstDate = datetime.datetime.strptime(firstDate, '%Y-%m-%d').date()
                secondDate = datetime.datetime.strptime(secondDate, '%Y-%m-%d').date()
            except ValueError:
                return Response({'error': 'Invalid date format. Use YYYY-MM-DD.'}, status=status.HTTP_400_BAD_REQUEST)
            queryset = queryset.objects.filter(date__lte=firstDate + secondDate)
            return queryset

        if 'secondDate' in self.request.GET:
            secondDate = self.request.GET.get('secondDate')
            try:
                secondDate = datetime.datetime.strptime(secondDate, '%Y-%m-%d').date()
            except ValueError:
                return Response({'error': 'Invalid date format. Use YYYY-MM-DD.'}, status=status.HTTP_400_BAD_REQUEST)
            queryset = queryset.objects.filter(date=secondDate)
            return queryset

        if 'firstDate' in self.request.GET:
            firstDate = self.request.GET.get('firstDate')
            try:
                firstDate = datetime.datetime.strptime(firstDate, '%Y-%m-%d').date()
            except ValueError:
                return Response({'error': 'Invalid date format. Use YYYY-MM-DD.'}, status=status.HTTP_400_BAD_REQUEST)
            queryset = queryset.objects.filter(date__lte=firstDate + timezone.now().date())
            return queryset

        return queryset


class AbnormalView(generics.ListAPIView):
    queryset = Abnormal.objects.all()
    serializer_class = AbnormalSerializer

    permission_classes = [IsAuthenticated]

    pagination_class = MyAPIListPagination

    def get_queryset(self):
        city = 'Воронеж'
        country = 'Россия'

        """Если пользователь зареган и у него есть страна/город взять от него """
        if self.request.user.is_authenticated:
            modelUser = get_user_model()
            user = modelUser.objects.get(pk=self.request.user.pk)
            if user.city:
                city = user.city
            if user.country:
                country = user.country

        if 'city' in self.request.GET:
            city = self.request.GET['city']
        if 'country' in self.request.GET:
            country = self.request.GET['country']

        queryset = self.queryset.objects.filter(city__city=city, city__country=country)

        if 'firstYear' in self.request.GET and 'secondYear' in self.request.GET:
            firstYear = self.request.GET.get('firstYear')
            secondYear = self.request.GET.get('secondYear')
            if firstYear.isdigit() and len(firstYear) <= 4 and secondYear.isdigit() and len(secondYear) <= 4:
                """year__lte - норм?"""
                queryset = queryset.objects.filter(year__lte=firstYear + secondYear).select_related('minT', 'maxT',
                                                                                                    'maxWS',
                                                                                                    'maxP').exclude(
                    id=None).exclude(
                    city=None).values('year', 'minT__date', 'minT__minTem', 'maxT__date', 'maxT__maxTem', 'maxWS__date',
                                      'maxWS__windSpeed', 'maxP__date', 'maxP__precipitation')

                # queryset = queryset.objects.filter(year__lte=firstYear + secondYear).select_related('minT__date',
                #                                                                                     'minT__minTem',
                #                                                                                     'maxT__date',
                #                                                                                     'maxT__maxTem',
                #                                                                                     'maxWS__date',
                #                                                                                     'maxWS__windSpeed',
                #                                                                                     'maxP__date',
                #                                                                                     'maxP__precipitation')
            else:
                return Response({'error': 'Invalid date format. Use YYYY.'}, status=status.HTTP_400_BAD_REQUEST)
            return queryset

        if 'firstYear' in self.request.GET:
            firstYear = self.request.GET.get('firstYear')
            if firstYear.isdigit() and len(firstYear) <= 4:
                """year__lte - норм?"""
                """получить int года сейчас"""
                queryset = queryset.objects.filter(year__lte=firstYear + 2023).select_related('minT', 'maxT', 'maxWS',
                                                                                              'maxP').exclude(
                    id=None).exclude(
                    city=None).values('year', 'minT__date', 'minT__minTem', 'maxT__date', 'maxT__maxTem', 'maxWS__date',
                                      'maxWS__windSpeed', 'maxP__date', 'maxP__precipitation')
            else:
                return Response({'error': 'Invalid date format. Use YYYY.'}, status=status.HTTP_400_BAD_REQUEST)
            return queryset

        if 'secondYear' in self.request.GET:
            secondYear = self.request.GET.get('secondYear')
            if secondYear.isdigit() and len(secondYear) <= 4:
                """year__lte - норм?"""
                queryset = queryset.objects.filter(year=secondYear).select_related('minT', 'maxT', 'maxWS',
                                                                                   'maxP').exclude(
                    id=None).exclude(
                    city=None).values('year', 'minT__date', 'minT__minTem', 'maxT__date', 'maxT__maxTem', 'maxWS__date',
                                      'maxWS__windSpeed', 'maxP__date', 'maxP__precipitation')
            else:
                return Response({'error': 'Invalid date format. Use YYYY.'}, status=status.HTTP_400_BAD_REQUEST)
            return queryset

        return queryset


class SetViewEmailSuperUser(APIView):
    def get(self, request, *args, **kwargs):
        if request.user.is_superuser:
            modelUser = get_user_model()
            user = modelUser.objects.get(email=request.user.email)
            return Response({'email': user.email})
        return Response({'error': 'Incorrect password'})


class UserViewSets(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    permission_classes = [IsAdminUser]
    pagination_class = MyAPIListPagination
    pagination_class.page_size = 10


class AdvertisementAPIView(APIView):
    def get(self, request, *args, **kwargs):
        if request.user.is_superuser:
            """выдать страниицы для выбора, где заменять рекламу"""
        return Response({'error': 'Incorrect password'})

    def post(self, request, *args, **kwargs):
        if request.user.is_superuser:
            """заменить img рекламы"""
        return Response({'error': 'Incorrect password'})


class SetNewPass(APIView):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            modelUser = get_user_model()
            nicknameUser = modelUser.objects.get(nickname=request.user.nickname)
            emailUser = modelUser.objects.get(email=request.user.email)
            return Response({'nickname': nicknameUser}, {'email': emailUser})
        return Response({'error': 'Incorrect password'})

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return Response({'error': 'Incorrect password'})
        q = User.objects.all()
        user = q.get(nickname=f'+{request.data.get("nickname")}')

        res = Response(status=status.HTTP_404_NOT_FOUND)
        if 'city' in request.data:
            user.city = request.data.get("city")
            user.save()
            res = Response(status=status.HTTP_200_OK)

        if 'country' in request.data:
            user.country = request.data.get("country")
            user.save()
            res = Response(status=status.HTTP_200_OK)

        if res.status_code == status.HTTP_200_OK:
            return res

        if user.password == request.data.get("password") and 'pass' in request.data:
            user.set_password(request.data.get("pass"))
            """pass - новый пароль!!!"""
            user.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return res


class SetViewNicknameUser(APIView):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            modelUser = get_user_model()
            nicknameUser = modelUser.objects.get(nickname=request.user.nickname)
            return Response({'nickname': nicknameUser})
        return Response({'error': 'Incorrect password'})


class UserRegister(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        clean_data = custom_validation(request.data)
        serializer = UserRegisterSerializer(data=clean_data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.create(clean_data)
            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class UserLogin(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = (SessionAuthentication,)

    def post(self, request):
        data = request.data
        assert validate_nickname(data)
        assert validate_password(data)
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.check_user(data)
            login(request, user)
            return Response(serializer.data, status=status.HTTP_200_OK)


class UserLogout(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()

    def post(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)


class UserView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (SessionAuthentication,)

    ##
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response({'user': serializer.data}, status=status.HTTP_200_OK)


@login_required(login_url='/userprofile/login/')
def user_delete(request, id):
    user = User.objects.get(id=id)
    # Убедитесь, что вошедший в систему пользователь и удаляемый пользователь совпадают
    if request.user == user:
        # Выход, удаление данных и возврат в список блогов
        logout(request)
        user.delete()
        return redirect("article:article_list")
    else:
        return HttpResponse("У вас нет разрешения на удаление операций.")


def pageNotFound(request, exception):
    return HttpResponseNotFound(f"<h1>Страница не найдена</h1>")
