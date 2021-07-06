from django.urls import path

from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('addbirthday/', views.addBirthday, name='addBirthday'),
  path('updatebirthday/<int:pk>/', views.updateBirthday, name='updateBirthday'),
]