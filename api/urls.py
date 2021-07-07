from django.urls import path
from . import views
urlpatterns = [
  path('api/', views.birthdayList),
  path('api/birthday-list/', views.birthdayList),
  path('api/birthday/<int:pk>/', views.detail)
]