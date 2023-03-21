from django.contrib import admin

# Register your models here.
from .models import Preferences, Reviews, Tinder, Tour, TourShots, Type
admin.site.register(Preferences)
admin.site.register(Reviews)
admin.site.register(Tinder)
admin.site.register(Tour)
admin.site.register(TourShots)
admin.site.register(Type)