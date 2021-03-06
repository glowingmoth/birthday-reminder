import birthdays
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView


urlpatterns = [

    path('admin/', admin.site.urls, name='admin'),
    path('', include('api.urls')),
    path('', include('birthdays.urls')),
    path('', include('users.urls')),
]
