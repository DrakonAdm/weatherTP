from django.urls import path, re_path, include
from django.contrib import admin
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenVerifyView, TokenRefreshView

from .views import *
from django.contrib.auth import views
from rest_framework import routers

from terminator.yasg import urlpatterns1
# работает и так

app_name = 'terminatorWeather'

router = routers.SimpleRouter()
router.register(r'listUser', UserViewSets)


# авторизация и аунтификация через Token
#     path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
#     path('auth/', include('djoser.urls.jwt')),
#     re_path(r'^auth/', include('djoser.urls.authtoken')),
#     path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
#     path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
#     path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

urlpatterns = [

    # advertisement
    path('advertisementGET/', ImageAPIView.as_view(), name='advertisementGET'),  # get - выдача файла

    path('listCC/', GetViewAPICountryCity.as_view(), name='listCC'),  # списки стран и городов
    path('listCity/', GetViewAPICity.as_view(), name='listCity'),  # списки городов

    # авторизация и аутентификация по простому https://github.com/dotja/authentication_app_react_django_rest
    path('register/', UserRegister.as_view(), name='register'),
    path('login/', UserLogin.as_view(), name='login'),
    path('logout/', UserLogout.as_view(), name='logout'),
    # на всякий случай
    # path('user/', UserView.as_view(), name='user'),

    # обработка изменений User от админа
    # обработка изменений User от админа
    path('', include(router.urls)),
    # path('api-user/', include('rest_framework.urls', namespace='rest_framework')),

    # сортировка по today, tomorrow and definiteDAY
    path('today/', ForecastDayAPIView.as_view(), name='today'),  # главная страница
    path('tomorrow/', ForecastDayAPIView.as_view(), name='tomorrow'),
    path('date/', ForecastDayAPIView.as_view(), name='date'),  # прогноз на искомый день PastView

    path('days/', ForecastManyDayAPIView.as_view(), name='days'),  # главная страница (прогноз на 5 дней)
    # path('month/', ForecastManyDayAPIView.as_view(), name='month'),  # главная страница (прогноз на месяц)

    path('statisticPast/', PastView.as_view(), name='statisticPast'),  # статистика прошедшей погоды
    path('statisticAbnormal/', AbnormalView.as_view(), name='statisticAbnormal'),  # статистика аномальной погоды

    # просто выдаёт nickname пользователя или почту, если nickname нет
    path('choiceUser/', SetViewNicknameUser.as_view(), name='choiceUser'),
    # new passwort
    path('accountUser/', SetNewPass.as_view(), name='accountUser'),  # личный кабинет пользователя со сменой пароля
    # выбор статистики погоды SetViewEmailSuperUser
    # просто выдаёт email superuser
    path('emailSuperUser/', SetViewEmailSuperUser.as_view(), name='emailSuperUser'),  # выбор статистики погоды
]

urlpatterns += urlpatterns1
# http://127.0.0.1:8000/swagger/

# handler404 = pageNotFound

# urlpatterns += router.urls
