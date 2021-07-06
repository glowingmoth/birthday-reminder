from django.urls import path

from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('addbirthday/', views.addBirthday, name='addBirthday'),
  path('<int:oldfish>/update', views.updateBirthday, name='updateBirthday'),
]