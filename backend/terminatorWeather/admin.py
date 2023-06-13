from django.contrib import admin
from .models import Forecast, Location, Past, Abnormal, User, Advertisement

admin.site.register(User)

admin.site.register(Advertisement)
admin.site.register(Forecast)
admin.site.register(Location)
admin.site.register(Past)
admin.site.register(Abnormal)
