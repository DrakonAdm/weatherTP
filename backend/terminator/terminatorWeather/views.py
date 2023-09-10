from datetime import timedelta

from django.contrib.auth import logout, login
from django.contrib.auth.hashers import check_password
from django.db.models import F
from django.db.models import Value, CharField
from django.http import FileResponse, JsonResponse
from django.template.defaulttags import csrf_token
from django.utils import timezone
from django.utils.datetime_safe import datetime
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework import status, generics, viewsets, permissions
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

# from .Clothes.forecastClothes import ForecastClothes
from .forecastClothes import forecastClothes
from .swagger_docs import *
from .validations import *


class MyAPIListPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 10000


class ForecastDayAPIView(generics.ListAPIView):
    queryset = Forecast.objects.all()
    serializer_class = ForecastSerializer

    permission_classes = (permissions.AllowAny,)

    @weather_forecast_day
    def get(self, request, *args, **kwargs):
        city = ''
        country = ''

        """Если пользователь зареган и у него есть страна/город взять от него """
        if request.user.is_authenticated:
            user = get_user_model().objects.get(email=request.user.email)
            if user.city and user.country:
                city = user.city
                country = user.country

        if 'city' in request.query_params and 'country' in request.query_params:
            city = request.query_params['city']
            country = request.query_params['country']

        if 'date' in request.query_params:
            dateSearch = request.query_params.get('date')
        elif 'tomorrow' in request.query_params:
            """возможно фронт не передаст завтрашнюю дату"""
            dateSearch = timezone.now().date() + timedelta(days=1)
            # dateSearch = request.query_params.get('tomorrow')
        else:
            dateSearch = timezone.now().date()

        try:
            dateSearch = datetime.strptime(str(dateSearch), '%Y-%m-%d').date()
        except ValueError:
            return JsonResponse({'error': 'Invalid date format. Use YYYY-MM-DD.'}, status=status.HTTP_400_BAD_REQUEST)

        """передан только город"""
        if 'city' in request.query_params and 'country' not in request.query_params:
            city = request.query_params['city']
            queryset = Forecast.objects.filter(date=dateSearch, city__city=city)
        else:
            queryset = Forecast.objects.filter(date=dateSearch, city__city=city, city__country=country)

        if not queryset.exists():
            queryset = Forecast.objects.filter(date=dateSearch, city__city="Воронеж")

        if not queryset.exists():
            return JsonResponse(
                {'error': 'Что-то с датой'},
                status=status.HTTP_404_NOT_FOUND)

        maxStr, averageStr, minStr = forecastClothes(queryset)

        print(maxStr, averageStr, minStr)
        queryset = queryset.annotate(maxClothes=models.Value(maxStr, output_field=models.CharField()))
        queryset = queryset.annotate(averageClothes=models.Value(averageStr, output_field=models.CharField()))
        queryset = queryset.annotate(minClothes=models.Value(minStr, output_field=models.CharField()))

        queryset = queryset.annotate(city__city=F('city__city'))
        data = {'results': list(queryset.values())}
        return JsonResponse(data)


class ForecastManyDayAPIView(generics.ListAPIView):
    queryset = Forecast.objects.all()
    serializer_class = ForecastSerializer

    pagination_class = MyAPIListPagination
    permission_classes = (permissions.AllowAny,)

    @weather_forecast_days
    def get(self, request, *args, **kwargs):
        city = ''
        country = ''

        """Если пользователь зареган и у него есть страна/город взять от него """
        if request.user.is_authenticated:
            user = get_user_model().objects.get(email=request.user.email)
            if user.city and user.country:
                city = user.city
                country = user.country

        if 'city' in request.query_params and 'country' in request.query_params:
            city = request.query_params['city']
            country = request.query_params['country']

        dateSearchFirst = timezone.now().date()
        dateSearchSecond = timezone.now().date() + timedelta(days=5)
        try:
            dateSearchFirst = datetime.strptime(str(dateSearchFirst), '%Y-%m-%d').date()
            dateSearchSecond = datetime.strptime(str(dateSearchSecond), '%Y-%m-%d').date()
        except ValueError:
            return JsonResponse({'error': 'Invalid date format. Use YYYY-MM-DD.'}, status=status.HTTP_400_BAD_REQUEST)

        """передан только город"""
        if 'city' in request.query_params and 'country' not in request.query_params:
            city = request.query_params['city']
            queryset = Forecast.objects.filter(city__city=city, date__gte=dateSearchFirst, date__lte=dateSearchSecond)
        else:
            queryset = Forecast.objects.filter(city__city=city, city__country=country, date__gte=dateSearchFirst,
                                               date__lte=dateSearchSecond)
        # if 'days' in request.query_params:
        #     queryset = queryset.filter(date__lte=timezone.now().date() + timedelta(days=9))

        if not queryset.exists():
            city = "Воронеж"
            queryset = Forecast.objects.filter(city__city="Воронеж", date__gte=dateSearchFirst,
                                               date__lte=dateSearchSecond)

        if not queryset.exists():
            return JsonResponse(
                {'error': 'Что-то с датой'},
                status=status.HTTP_404_NOT_FOUND)

        data = {
            'city': city,
            'forecast_data': []  # Здесь можно добавить фактические данные прогноза
        }

        paginated_queryset = self.paginate_queryset(queryset)
        serializer = self.serializer_class(paginated_queryset, many=True)
        serialized_data = serializer.data

        data['forecast_data'] = serialized_data

        return JsonResponse(data)


class PastView(generics.ListAPIView):
    queryset = Past.objects.all()
    serializer_class = PastSerializer

    permission_classes = (permissions.AllowAny,)

    pagination_class = MyAPIListPagination

    @statistic_past
    def get(self, request, *args, **kwargs):
        city = ''
        country = ''

        """Если пользователь зареган и у него есть страна/город взять от него """
        if request.user.is_authenticated:
            user = get_user_model().objects.get(email=request.user.email)
            if user.city and user.country:
                city = user.city
                country = user.country

        if 'city' in request.query_params and 'country' in request.query_params:
            city = request.query_params['city']
            country = request.query_params['country']

        """передан только город"""
        if 'city' in request.query_params and 'country' not in request.query_params:
            city = request.query_params['city']
            queryset = Past.objects.filter(city__city=city)
        else:
            queryset = Past.objects.filter(city__city=city, city__country=country)

        if not queryset.exists():
            queryset = Past.objects.filter(city__city="Воронеж")

        if not queryset.exists():
            return JsonResponse(
                {'error': 'Просто как ты сюда попал??'},
                status=status.HTTP_404_NOT_FOUND)

        if 'firstDate' in request.query_params and 'secondDate' in request.query_params:
            firstDate = request.query_params.get('firstDate')
            secondDate = request.query_params.get('secondDate')
            try:
                firstDate = datetime.strptime(str(firstDate), '%Y-%m-%d').date()
                secondDate = datetime.strptime(str(secondDate), '%Y-%m-%d').date()
            except ValueError:
                return JsonResponse({'error': 'Invalid date format. Use YYYY-MM-DD.'},
                                    status=status.HTTP_400_BAD_REQUEST)
            if not queryset.filter(date=firstDate).exists() or not queryset.filter(
                    date=secondDate).exists():
                return JsonResponse(
                    {'error': f'Простите, на таких дат {firstDate} {secondDate} нет в нашей базе'},
                    status=status.HTTP_404_NOT_FOUND)

            queryset = queryset.filter(date__gte=firstDate, date__lte=secondDate)

            if not queryset.exists():
                return JsonResponse(
                    {'error': 'Простите, вы либо указали неверную дату, либо данного города нет в нашей базе'},
                    status=status.HTTP_404_NOT_FOUND)

            queryset = queryset.annotate(city__city=F('city__city'))
            paginated_queryset = self.paginate_queryset(queryset)
            serializer = self.serializer_class(paginated_queryset, many=True)
            return self.get_paginated_response(serializer.data)

        if 'secondDate' in request.query_params:
            secondDate = request.query_params.get('secondDate')
            try:
                secondDate = datetime.strptime(str(secondDate), '%Y-%m-%d').date()
            except ValueError:
                return JsonResponse({'error': 'Invalid date format. Use YYYY-MM-DD.'},
                                    status=status.HTTP_400_BAD_REQUEST)

            if not queryset.filter(date=secondDate).exists():
                return JsonResponse(
                    {'error': f'Простите, на такой даты {secondDate} нет в нашей базе'},
                    status=status.HTTP_404_NOT_FOUND)

            queryset = queryset.filter(date=secondDate)

            if not queryset.exists():
                return JsonResponse(
                    {'error': 'Простите, вы либо указали неверную дату, либо данного города нет в нашей базе'},
                    status=status.HTTP_404_NOT_FOUND)

            queryset = queryset.annotate(city__city=F('city__city'))
            paginated_queryset = self.paginate_queryset(queryset)
            serializer = self.serializer_class(paginated_queryset, many=True)
            return self.get_paginated_response(serializer.data)

        if 'firstDate' in request.query_params:
            firstDate = request.query_params.get('firstDate')
            try:
                firstDate = datetime.strptime(str(firstDate), '%Y-%m-%d').date()
            except ValueError:
                return JsonResponse({'error': 'Invalid date format. Use YYYY-MM-DD.'},
                                    status=status.HTTP_400_BAD_REQUEST)

            if not queryset.filter(date=firstDate).exists():
                return JsonResponse(
                    {'error': f'Простите, на такой даты {firstDate} нет в нашей базе'},
                    status=status.HTTP_404_NOT_FOUND)
            queryset = queryset.filter(date__gte=firstDate, date__lte=timezone.now().date())

            if not queryset.exists():
                return JsonResponse(
                    {'error': 'Простите, вы либо указали неверную дату, либо данного города нет в нашей базе'},
                    status=status.HTTP_404_NOT_FOUND)

            queryset = queryset.annotate(city__city=F('city__city'))
            paginated_queryset = self.paginate_queryset(queryset)
            serializer = self.serializer_class(paginated_queryset, many=True)
            return self.get_paginated_response(serializer.data)

        queryset = queryset.annotate(city__city=F('city__city'))
        paginated_queryset = self.paginate_queryset(queryset)
        serializer = self.serializer_class(paginated_queryset, many=True)
        return self.get_paginated_response(serializer.data)


class AbnormalView(generics.ListAPIView):
    queryset = Abnormal.objects.all()
    serializer_class = AbnormalSerializer

    # permission_classes = [IsAuthenticated]
    permission_classes = (permissions.AllowAny,)

    pagination_class = MyAPIListPagination

    @statistic_abnormal
    def get(self, request, *args, **kwargs):
        city = 'Воронеж'
        country = 'Россия'

        # """Если пользователь зареган и у него есть страна/город взять от него """
        # if request.user.is_authenticated:
        #     user = get_user_model().objects.get(email=request.user.email)
        #     if user.city and user.country:
        #         city = user.city
        #         country = user.country

        if request.query_params.get("city") and request.query_params.get("country"):
            city = request.query_params['city']
            country = request.query_params['country']

        if request.query_params.get("city") and request.query_params.get("country"):
            city = request.query_params['city']
            queryset = Abnormal.objects.filter(city__city=city)
        else:
            queryset = Abnormal.objects.filter(city__city=city, city__country=country)

        if not queryset.exists():
            queryset = Abnormal.objects.filter(city__city="Воронеж")

        if not queryset.exists():
            return JsonResponse(
                {'error': 'Просто как ты сюда попал??'},
                status=status.HTTP_404_NOT_FOUND)

        if request.query_params.get("firstYear") and request.query_params.get("secondYear"):
            firstYear = request.query_params.get('firstYear')
            secondYear = request.query_params.get('secondYear')
            if firstYear.isdigit() and len(firstYear) == 4 and secondYear.isdigit() and len(secondYear) == 4:
                """year__lte - норм?"""
                queryset = queryset.filter(year__gte=firstYear, year__lte=secondYear)
                queryset = queryset.select_related('city',
                                                   'minT',
                                                   'maxT',
                                                   'maxWS',
                                                   'maxP').annotate(
                    min_tem=F('minT__minTem'),
                    max_tem=F('maxT__maxTem'),
                    max_wind_speed=F('maxWS__windSpeed'),
                    precipitation=F('maxP__precipitation'),
                    city__city=F('city__city'),
                    min_tem_date=F('minT__date'),
                    max_tem_date=F('maxT__date'),
                    max_wind_speed_date=F('maxWS__date'),
                    precipitation_date=F('maxP__date')
                )

            else:
                return JsonResponse({'error': 'Invalid date format. Use YYYY.'}, status=status.HTTP_400_BAD_REQUEST)

            if not queryset.exists():
                return JsonResponse(
                    {'error': 'Простите, вы либо указали неверную дату, либо данного города нет в нашей базе'},
                    status=status.HTTP_404_NOT_FOUND)

            queryset = queryset.annotate(city__city=F('city__city'))
            data = {'results': list(queryset.values())}
            return JsonResponse(data)

        if request.query_params.get("firstYear") and not request.query_params.get("secondYear"):
            firstYear = request.query_params.get('firstYear')
            if firstYear.isdigit() and len(firstYear) == 4:
                """year__lte - норм?"""
                """получить int года сейчас"""
                queryset = queryset.filter(year__gte=firstYear, year__lte=2023)
                queryset = queryset.select_related('city', 'minT',
                                                   'maxT', 'maxWS',
                                                   'maxP').annotate(
                    min_tem=F('minT__minTem'),
                    max_tem=F('maxT__maxTem'),
                    max_wind_speed=F('maxWS__windSpeed'),
                    precipitation=F('maxP__precipitation'),
                    city__city=F('city__city'),
                    min_tem_date=F('minT__date'),
                    max_tem_date=F('maxT__date'),
                    max_wind_speed_date=F('maxWS__date'),
                    precipitation_date=F('maxP__date')
                )
            else:
                return JsonResponse({'error': 'Invalid date format. Use YYYY.'}, status=status.HTTP_400_BAD_REQUEST)

            if not queryset.exists():
                return JsonResponse(
                    {'error': 'Простите, вы либо указали неверную дату, либо данного города нет в нашей базе'},
                    status=status.HTTP_404_NOT_FOUND)
            queryset = queryset.annotate(city__city=F('city__city'))
            data = {'results': list(queryset.values())}
            return JsonResponse(data)

        if request.query_params.get("secondYear") and not request.query_params.get("firstYear"):
            secondYear = request.query_params.get('secondYear')
            if secondYear.isdigit() and len(secondYear) == 4:
                """year__lte - норм?"""
                queryset = queryset.filter(year=secondYear)
                queryset = queryset.select_related('city', 'minT', 'maxT', 'maxWS',
                                                   'maxP').annotate(
                    min_tem=F('minT__minTem'),
                    max_tem=F('maxT__maxTem'),
                    max_wind_speed=F('maxWS__windSpeed'),
                    precipitation=F('maxP__precipitation'),
                    city__city=F('city__city'),
                    min_tem_date=F('minT__date'),
                    max_tem_date=F('maxT__date'),
                    max_wind_speed_date=F('maxWS__date'),
                    precipitation_date=F('maxP__date')
                )
            else:
                return JsonResponse({'error': 'Invalid date format. Use YYYY.'}, status=status.HTTP_400_BAD_REQUEST)

            if not queryset.exists():
                return JsonResponse(
                    {'error': 'Простите, вы либо указали неверную дату, либо данного города нет в нашей базе'},
                    status=status.HTTP_404_NOT_FOUND)
            queryset = queryset.annotate(city__city=F('city__city'))
            data = {'results': list(queryset.values())}
            return JsonResponse(data)

        queryset = queryset.select_related('city', 'minT', 'maxT', 'maxWS', 'maxP').annotate(
            min_tem=F('minT__minTem'),
            max_tem=F('maxT__maxTem'),
            max_wind_speed=F('maxWS__windSpeed'),
            precipitation=F('maxP__precipitation'),
            city__city=F('city__city'),
            min_tem_date=F('minT__date'),
            max_tem_date=F('maxT__date'),
            max_wind_speed_date=F('maxWS__date'),
            precipitation_date=F('maxP__date')
        )

        queryset = queryset.annotate(city__city=F('city__city'))
        data = {'results': list(queryset.values())}
        return JsonResponse(data)


class SetViewEmailSuperUser(APIView):
    @email_sudouser_get
    def get(self, request, *args, **kwargs):
        if request.user.is_superuser:
            user = get_user_model().objects.get(email=request.user.email)
            return JsonResponse({'email': user.email})
        return JsonResponse({'error': 'Incorrect password'})


class GetViewAPICity(APIView):
    permission_classes = (permissions.AllowAny,)

    @city_get
    def get(self, request, *args, **kwargs):
        cities = Location.objects.values_list('city', flat=True)
        return JsonResponse({'cities': list(cities)})


class GetViewAPICountryCity(APIView):
    permission_classes = (permissions.AllowAny,)

    @country_city_get
    def get(self, request, *args, **kwargs):
        cities = Location.objects.filter()
        serializer = LocationSerializer(cities, many=True)
        return Response(serializer.data)

    # @country_city_get
    # def get(self, request, *args, **kwargs):
    #     if 'country' in request.query_params:
    #         # If 'country' key is present, return sorted list of cities for that country
    #         cities = Location.objects.filter(country=request.query_params['country']).order_by('city')
    #         serializer = LocationSerializer(cities, many=True)
    #         return Response(serializer.data)
    #     else:
    #         # If 'country' key is not present, return list of countries
    #         countries = Location.objects.values('country').distinct().order_by('country')
    #         return JsonResponse({'countries': [c['country'] for c in countries]})


class UserViewSets(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    permission_classes = [IsAdminUser]
    pagination_class = MyAPIListPagination
    pagination_class.page_size = 10


class ImageAPIView(APIView):
    permission_classes = (permissions.AllowAny,)

    @advertisement_get
    def get(self, request, *args, **kwargs):
        short = request.query_params.get('short')
        try:
            print(short)
            advertisement = Advertisement.objects.get(short=short)
            print(advertisement.page)
            file_path = advertisement.page.path
            file_type = file_path.split('.')[-1].lower()
            if file_type == 'jpeg':
                content_type = 'image/jpeg'
            elif file_type == 'png':
                content_type = 'image/png'
            else:
                return JsonResponse({'error': 'Invalid file type'}, status=status.HTTP_400_BAD_REQUEST)
            return FileResponse(open(file_path, 'rb'), content_type=content_type)
        except Advertisement.DoesNotExist:
            return JsonResponse({'error': 'Advertisement not found'}, status=status.HTTP_404_NOT_FOUND)
        except FileNotFoundError:
            return JsonResponse({'error': 'Image not found'}, status=status.HTTP_404_NOT_FOUND)


class SetNewPass(APIView):
    permission_classes = (permissions.AllowAny, )

    # permission_classes = [IsAuthenticated]
    # authentication_classes = (SessionAuthentication, )

    @redefinition_post
    def get(self, request, *args, **kwargs):
        if not request.query_params.get("email") and not request.query_params.get("password"):
            return JsonResponse({'error': 'Incorrect token'}, status=status.HTTP_401_UNAUTHORIZED)

        user = get_user_model().objects.get(email=request.query_params.get("email"))
        password = request.query_params.get("password")

        res = False

        if request.query_params.get("city"):
            user.city = request.query_params.get("city")
            user.save()
            res = True

        if request.query_params.get("country"):
            user.country = request.query_params.get("country")
            user.save()
            res = True

        # if request.query_params.get("nickname"):
        #     user.nickname = request.query_params.get("nickname")
        #     user.save()
        #     res = True

        if request.query_params.get("pass"):
            if not check_password(request.query_params.get("password"), user.password):
                return JsonResponse({'error': 'Вы ввели неверный пароль'}, status=status.HTTP_404_NOT_FOUND)
            user.set_password(request.query_params.get("pass"))
            """pass - новый пароль!!!"""
            user.save()
            password = request.query_params.get("pass")
            res = True

        if res:
            data = {'nickname': user.nickname,
                    'password': password,
                    'email': user.email,
                    'country': user.country,
                    'city': user.city}
            serializer = UserSerializer()
            return Response(serializer.to_representation(data), status=status.HTTP_200_OK)
        else:
            return JsonResponse({'error': 'Incorrect password'}, status=status.HTTP_400_BAD_REQUEST)

        # @nickname_email_user_get
        # def get(self, request, *args, **kwargs):
        #     if request.user.is_authenticated:
        #         modelUser = get_user_model().objects.get(email=request.user.email)
        #         nicknameUser = "Вы не добавили"
        #         if 'nickname' in request.query_params:
        #             nicknameUser = modelUser.nickname
        #         emailUser = modelUser.email
        #         # return Response({'nickname': nicknameUser, 'email': emailUser})
        #         data = {'nickname': nicknameUser, 'email': emailUser}
        #         serializer = UserSerializer()
        #         return Response(serializer.to_representation(data))
        #     else:
        #         return JsonResponse({'error': 'Вы не авторизованы'}, status=status.HTTP_401_UNAUTHORIZED)


class SetViewNicknameUser(APIView):
    @nickname_user_get
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            modelUser = get_user_model().objects.get(email=request.user.email)
            if 'nickname' in request.query_params:
                return JsonResponse({'nickname': modelUser.nickname})
            return JsonResponse({'nickname': modelUser.email})
        return JsonResponse({'error': 'Incorrect password'})


class UserRegister(APIView):
    permission_classes = (permissions.AllowAny,)

    @registration_user
    def post(self, request):
        try:
            clean_data = custom_validation(request.query_params)
        except ValidationError as e:
            return JsonResponse({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        serializer = UserRegisterSerializer(data=clean_data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.create(clean_data)
            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse({'error': 'Failed'}, status=status.HTTP_400_BAD_REQUEST)


class UserLogin(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = (SessionAuthentication,)

    @login_user
    def post(self, request):
        email = request.query_params.get('email')
        password = request.query_params.get('password')

        model = User.objects.filter(email=email).first()
        if not model:
            return Response({'detail': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)

        data = {
            'email': email,
            'password': password,
            'nickname': model.nickname,
        }

        if model.city:
            data['city'] = model.city
        if model.country:
            data['country'] = model.country

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
        return JsonResponse({'message': 'Logged out successfully'}, status=status.HTTP_200_OK)
        # if request.user.is_authenticated:
        #     logout(request)
        #     return JsonResponse({'message': 'Logged out successfully'}, status=status.HTTP_200_OK)
        # else:
        #     return JsonResponse({'message': 'Logged out failed (You are not authenticate)'},
        #                         status=status.HTTP_400_BAD_REQUEST)

# class UserView(APIView):
#     permission_classes = (permissions.IsAuthenticated,)
#     authentication_classes = (SessionAuthentication,)
#
#     def get(self, request):
#         serializer = UserSerializer(request.user)
#         return Response({'user': serializer.data}, status=status.HTTP_200_OK)

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
