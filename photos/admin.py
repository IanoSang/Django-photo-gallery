from django.contrib import admin

# Register your models here.
from .models import Category, Photo, Location

admin.site.register(Category),
admin.site.register(Photo),
admin.site.register(Location),
