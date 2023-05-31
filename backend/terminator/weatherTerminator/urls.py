from django.urls import path, re_path
from django.contrib import admin
from .views import *

app_name = 'weatherTerminator'
urlpatterns = [
    path('admin/', admin.site.urls, name='adminPanel'),





    # path('', index, name='home'),  # http://127.0.0.1:8000/
    # path('', Session_base.as_view(), name='base'),  # http://127.0.0.1:8000/cinema
    # path('film', Film_base.as_view(), name='cinema_film'),  # http://127.0.0.1:8000/cinema/film
    # path('film_company', Fc_base.as_view(), name='cinema_fc'),  # http://127.0.0.1:8000/cinema/film_company
    # path('contacts', cinema_contact, name='cinema_contact'),  # http://127.0.0.1:8000/cinema/contacts
    # path('buy/', Ticket_buy.as_view(), name='buy'),
    # path('login/', LoginUser.as_view(), name='login'),
    # path('register/', RegisterUser.as_view(), name='register'),
    # path('logout/', logout_user, name='logout'),
    # path('buy/confirm', confirm, name='confirm')



    # path('sens/<slug:hall>/', sessions),  # http://127.0.0.1:8000/sens/hall_one/
    # re_path(r'^archive/(?P<year>[0-9]{4})/', archive)  # http://127.0.0.1:8000/archive/2022/
]