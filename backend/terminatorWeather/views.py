import os
from django.http import FileResponse, JsonResponse, Http404
from django.conf import settings
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
from rest_framework.schemas import AutoSchema
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser

# from .Clothes.forecastClothes import ForecastClothes
from .forecastClothes import forecastClothes
from .models import *
from .serializers import *
from rest_framework import status, generics, viewsets, permissions

from .validations import *
from .swagger_docs import *
import coreapi


# class TodoListViewSchema(AutoSchema):
#     def get_manual_fields(self, path, method):
#         extra_fields = []
#         if method.lower() in ['post', 'get']:
#             extra_fields = [
#                 coreapi.Field('desc')
#             ]


class MyAPIListPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 10000


class ForecastDayAPIView(generics.ListAPIView):
    queryset = Forecast.objects.all()
    serializer_class = ForecastSerializer

    @weather_forecast_day
    def get(self, request, *args, **kwargs):
        city = 'Воронеж'
        country = 'Россия'

        """Если пользователь зареган и у него есть страна/город взять от него """
        if request.user.is_authenticated:
            modelUser = get_user_model()
            user = modelUser.objects.get(pk=request.user.pk)
            if user.city and user.country:
                city = user.city
                country = user.country

        if 'city' in request.GET and 'country' in request.GET:
            city = request.GET['city']
            country = request.GET['country']

        if 'date' in request.GET:
            dateSearch = request.GET.get('date')
        elif 'tomorrow' in request.GET:
            """возможно фронт не передаст завтрашнюю дату"""
            # dateSearch = timezone.now().date() + timedelta(days=1)
            dateSearch = request.GET.get('tomorrow')
        else:
            dateSearch = timezone.now().date()

        try:
            dateSearch = datetime.strptime(str(dateSearch), '%Y-%m-%d').date()
        except ValueError:
            return JsonResponse({'error': 'Invalid date format. Use YYYY-MM-DD.'}, status=status.HTTP_400_BAD_REQUEST)

        queryset = Forecast.objects.filter(date=dateSearch, city__city=city, city__country=country)
        if not queryset.exists():
            raise Http404("Простите, вы либо указали неверную дату, либо данного города нет в нашей базе")

        maxStr, averageStr, minStr = forecastClothes(queryset)

        queryset = queryset.annotate(maxTemperature=models.Value(maxStr, output_field=models.CharField()))
        queryset = queryset.annotate(averageTemperature=models.Value(averageStr, output_field=models.CharField()))
        queryset = queryset.annotate(minTemperature=models.Value(minStr, output_field=models.CharField()))

        """правильно ли возвращать queryset????"""
        # queryset = Forecast.objects.objects.filter(date=date)
        # serializer = serializer_class(queryset, many=True)
        # return Response(serializer.data)
        return queryset


class ForecastManyDayAPIView(generics.ListAPIView):
    queryset = Forecast.objects.all()
    serializer_class = ForecastSerializer

    pagination_class = MyAPIListPagination

    @weather_forecast_days
    def get(self, request, *args, **kwargs):
        city = 'Воронеж'
        country = 'Россия'

        """Если пользователь зареган и у него есть страна/город взять от него """
        if request.user.is_authenticated:
            modelUser = get_user_model()
            user = modelUser.objects.get(pk=request.user.pk)
            if user.city and user.country:
                city = user.city
                country = user.country

        if 'city' in request.GET and 'country' in request.GET:
            city = request.GET['city']
            country = request.GET['country']

        queryset = Forecast.objects.filter(city__city=city, city__country=country)
        if 'days' in request.GET:
            queryset = queryset.objects.filter(date__lte=timezone.now().date() + timedelta(days=9))

        if not queryset.exists():
            raise Http404("Простите, вы либо указали неверную дату, либо данного города нет в нашей базе")
        return queryset


class PastView(generics.ListAPIView):
    queryset = Past.objects.all()
    serializer_class = PastSerializer

    permission_classes = [IsAuthenticated]

    pagination_class = MyAPIListPagination

    @statistic_past
    def get(self, request, *args, **kwargs):
        city = 'Воронеж'
        country = 'Россия'

        """Если пользователь зареган и у него есть страна/город взять от него """
        if request.user.is_authenticated:
            modelUser = get_user_model()
            user = modelUser.objects.get(pk=request.user.pk)
            if user.city and user.country:
                city = user.city
                country = user.country

        if 'city' in request.GET and 'country' in request.GET:
            city = request.GET['city']
            country = request.GET['country']

        queryset = Past.objects.filter(city__city=city, city__country=country)

        if 'firstDate' in request.GET and 'secondDate' in request.GET:
            firstDate = request.GET.get('firstDate')
            secondDate = request.GET.get('secondDate')
            try:
                firstDate = datetime.strptime(str(firstDate), '%Y-%m-%d').date()
                secondDate = datetime.strptime(str(secondDate), '%Y-%m-%d').date()
            except ValueError:
                return JsonResponse({'error': 'Invalid date format. Use YYYY-MM-DD.'}, status=status.HTTP_400_BAD_REQUEST)
            queryset = queryset.objects.filter(date__gte=firstDate, date__lte=secondDate)

            if not queryset.exists():
                raise Http404("Простите, вы либо указали неверную дату, либо данного города нет в нашей базе")
            return queryset

        if 'secondDate' in request.GET:
            secondDate = request.GET.get('secondDate')
            try:
                secondDate = datetime.strptime(str(secondDate), '%Y-%m-%d').date()
            except ValueError:
                return JsonResponse({'error': 'Invalid date format. Use YYYY-MM-DD.'}, status=status.HTTP_400_BAD_REQUEST)
            queryset = queryset.objects.filter(date=secondDate)

            if not queryset.exists():
                raise Http404("Простите, вы либо указали неверную дату, либо данного города нет в нашей базе")
            return queryset

        if 'firstDate' in request.GET:
            firstDate = request.GET.get('firstDate')
            try:
                firstDate = datetime.strptime(str(firstDate), '%Y-%m-%d').date()
            except ValueError:
                return JsonResponse({'error': 'Invalid date format. Use YYYY-MM-DD.'}, status=status.HTTP_400_BAD_REQUEST)
            queryset = queryset.objects.filter(date__gte=firstDate, date__lte=timezone.now().date())

            if not queryset.exists():
                raise Http404("Простите, вы либо указали неверную дату, либо данного города нет в нашей базе")
            return queryset

        return queryset


class AbnormalView(generics.ListAPIView):
    queryset = Abnormal.objects.all()
    serializer_class = AbnormalSerializer

    permission_classes = [IsAuthenticated]

    pagination_class = MyAPIListPagination

    @statistic_abnormal
    def get(self, request, *args, **kwargs):
        city = 'Воронеж'
        country = 'Россия'

        """Если пользователь зареган и у него есть страна/город взять от него """
        if request.user.is_authenticated:
            modelUser = get_user_model()
            user = modelUser.objects.get(pk=request.user.pk)
            if user.city and user.country:
                city = user.city
                country = user.country

        if 'city' in request.GET and 'country' in request.GET:
            city = request.GET['city']
            country = request.GET['country']

        queryset = Abnormal.objects.filter(city__city=city, city__country=country)

        if 'firstYear' in request.GET and 'secondYear' in request.GET:
            firstYear = request.GET.get('firstYear')
            secondYear = request.GET.get('secondYear')
            if firstYear.isdigit() and len(firstYear) == 4 and secondYear.isdigit() and len(secondYear) == 4:
                """year__lte - норм?"""
                queryset = queryset.objects.filter(year__gte=firstYear, year__lte=secondYear).select_related('minT', 'maxT',
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
                return JsonResponse({'error': 'Invalid date format. Use YYYY.'}, status=status.HTTP_400_BAD_REQUEST)

            if not queryset.exists():
                raise Http404("Простите, вы либо указали неверную дату, либо данного города нет в нашей базе")
            return queryset

        if 'firstYear' in request.GET:
            firstYear = request.GET.get('firstYear')
            if firstYear.isdigit() and len(firstYear) == 4:
                """year__lte - норм?"""
                """получить int года сейчас"""
                queryset = queryset.objects.filter(year__gte=firstYear, year__lte=2023).select_related('minT', 'maxT', 'maxWS',
                                                                                              'maxP').exclude(
                    id=None).exclude(
                    city=None).values('year', 'minT__date', 'minT__minTem', 'maxT__date', 'maxT__maxTem', 'maxWS__date',
                                      'maxWS__windSpeed', 'maxP__date', 'maxP__precipitation')
            else:
                return JsonResponse({'error': 'Invalid date format. Use YYYY.'}, status=status.HTTP_400_BAD_REQUEST)

            if not queryset.exists():
                raise Http404("Простите, вы либо указали неверную дату, либо данного города нет в нашей базе")
            return queryset

        if 'secondYear' in request.GET:
            secondYear = request.GET.get('secondYear')
            if secondYear.isdigit() and len(secondYear) == 4:
                """year__lte - норм?"""
                queryset = queryset.objects.filter(year=secondYear).select_related('minT', 'maxT', 'maxWS',
                                                                                   'maxP').exclude(
                    id=None).exclude(
                    city=None).values('year', 'minT__date', 'minT__minTem', 'maxT__date', 'maxT__maxTem', 'maxWS__date',
                                      'maxWS__windSpeed', 'maxP__date', 'maxP__precipitation')
            else:
                return JsonResponse({'error': 'Invalid date format. Use YYYY.'}, status=status.HTTP_400_BAD_REQUEST)

            if not queryset.exists():
                raise Http404("Простите, вы либо указали неверную дату, либо данного города нет в нашей базе")
            return queryset

        if not queryset.exists():
            raise Http404("Простите, вы либо указали неверную дату, либо данного города нет в нашей базе")
        return queryset


class SetViewEmailSuperUser(APIView):
    @email_sudouser_get
    def get(self, request, *args, **kwargs):
        if request.user.is_superuser:
            modelUser = get_user_model()
            user = modelUser.objects.get(email=request.user.email)
            return JsonResponse({'email': user.email})
        return JsonResponse({'error': 'Incorrect password'})


class GetViewAPICountryCity(APIView):
    @country_city_get
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if 'country' in request.query_params:
                # If 'country' key is present, return sorted list of cities for that country
                cities = Location.objects.filter(country=request.query_params['country']).order_by('city')
                serializer = LocationSerializer(cities, many=True)
                return Response(serializer.data)
            else:
                # If 'country' key is not present, return list of countries
                countries = Location.objects.values('country').distinct().order_by('country')
                return JsonResponse({'countries': [c['country'] for c in countries]})
        return JsonResponse({'error': 'Incorrect password'})


class UserViewSets(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    permission_classes = [IsAdminUser]
    pagination_class = MyAPIListPagination
    pagination_class.page_size = 10


class AdvertisementAPIView(APIView):
    @advertisement_post
    def post(self, request, *args, **kwargs):
        if request.user.is_superuser:
            image_file = request.FILES['file']
            file_name = request.POST.get('file_name')
            if not file_name:
                return JsonResponse({'error': 'File name is required'})
            file_path = os.path.join(settings.STATIC_ROOT, 'image', file_name)
            with open(file_path, 'wb+') as destination:
                for chunk in image_file.chunks():
                    destination.write(chunk)
            return JsonResponse({'success': 'Image uploaded'})
        return JsonResponse({'error': 'Incorrect password'})

    # def post(self, request, *args, **kwargs):
    #     if request.user.is_superuser:
    #         image_file = request.FILES['file']
    #         file_path = os.path.join(settings.STATIC_ROOT, 'image', image_file.name)
    #         with open(file_path, 'wb+') as destination:
    #             for chunk in image_file.chunks():
    #                 destination.write(chunk)
    #         return JsonResponse({'success': 'Image uploaded'})
    #     return JsonResponse({'error': 'Incorrect password'})


class ImageAPIView(APIView):
    @advertisement_get
    def get(self, request, *args, **kwargs):
        image_name = kwargs.get('image_name')
        file_path = os.path.join(settings.STATIC_ROOT, 'image', image_name)
        try:
            return FileResponse(open(file_path, 'rb'), content_type='image/jpeg')
        except FileNotFoundError:
            return JsonResponse({'error': 'Image not found'}, status=status.HTTP_404_NOT_FOUND)


class SetNewPass(APIView):
    @nickname_email_user_get
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            modelUser = get_user_model()
            nicknameUser = "Вы не добавили"
            if 'nickname' in request.data:
                nicknameUser = modelUser.objects.get(nickname=request.user.nickname)
            emailUser = modelUser.objects.get(email=request.user.email)
            # return Response({'nickname': nicknameUser, 'email': emailUser})
            data = {'nickname': nicknameUser, 'email': emailUser}
            serializer = UserSerializer()
            return Response(serializer.to_representation(data))
        else:
            return JsonResponse({'error': 'Вы не авторизованы'}, status=status.HTTP_401_UNAUTHORIZED)

    @redefinition_post
    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return JsonResponse({'error': 'Incorrect password'})
        q = User.objects.all()
        user = q.get(email=f'+{request.data.get("email")}')

        res = JsonResponse(status=status.HTTP_404_NOT_FOUND)
        if 'city' in request.data:
            user.city = request.data.get("city")
            user.save()
            res = JsonResponse(status=status.HTTP_200_OK)

        if 'country' in request.data:
            user.country = request.data.get("country")
            user.save()
            res = JsonResponse(status=status.HTTP_200_OK)

        if 'nickname' in request.data:
            user.nickname = request.data.get("nickname")
            user.save()
            res = JsonResponse(status=status.HTTP_200_OK)

        if res.status_code == status.HTTP_200_OK:
            return res

        if user.password == request.data.get("password") and 'pass' in request.data:
            user.set_password(request.data.get("pass"))
            """pass - новый пароль!!!"""
            user.save()
            return JsonResponse(status=status.HTTP_200_OK)
        else:
            return res


class SetViewNicknameUser(APIView):
    @nickname_user_get
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            modelUser = get_user_model()
            if 'nickname' in request.data:
                nicknameUser = modelUser.objects.get(nickname=request.user.nickname)
                return JsonResponse({'nickname': nicknameUser.nickname})
            emailUser = modelUser.objects.get(email=request.user.email)
            return JsonResponse({'emailUser': emailUser.email})
        return JsonResponse({'error': 'Incorrect password'})


class UserRegister(APIView):
    permission_classes = (permissions.AllowAny,)

    @registration_user
    def post(self, request):
        clean_data = custom_validation(request.data)
        serializer = UserRegisterSerializer(data=clean_data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.create(clean_data)
            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(status=status.HTTP_400_BAD_REQUEST)


class UserLogin(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = (SessionAuthentication,)

    @login_user
    def post(self, request):
        data = request.data
        assert validate_email(data)
        assert validate_password(data)
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.check_user(data)
            login(request, user)
            return Response(serializer.data, status=status.HTTP_200_OK)


class UserLogout(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()

    @logout_user
    def post(self, request):
        logout(request)
        return JsonResponse(status=status.HTTP_200_OK)


class UserView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (SessionAuthentication,)

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response({'user': serializer.data}, status=status.HTTP_200_OK)


# @login_required(login_url='/userprofile/login/')
# def user_delete(request, id):
#     user = User.objects.get(id=id)
#     # Убедитесь, что вошедший в систему пользователь и удаляемый пользователь совпадают
#     if request.user == user:
#         # Выход, удаление данных и возврат в список блогов
#         logout(request)
#         user.delete()
#         return redirect("article:article_list")
#     else:
#         return HttpResponse("У вас нет разрешения на удаление операций.")
#
#
def pageNotFound(request, exception):
    return HttpResponseNotFound(f"<h1>Страница не найдена</h1>")
