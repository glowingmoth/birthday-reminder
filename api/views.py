from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import BirthdaySerializer
from birthdays.models import Birthday


@api_view(['GET'])
def apiOverview(request):
  api_urls = {
    'List': '/birthday-list/',
    'Detail': '/birthday/<int:pk>/',
    'Create': '/birthday-create/<int:pk>/',
    'Update': '/birthday-update/<int:pk>/',
    'Delete': '/birthday-delete/<int:pk>/',
  }
  return Response(api_urls)

@api_view(['GET'])
def birthdayList(request):
  birthdays = Birthday.objects.all()
  serializer = BirthdaySerializer(birthdays, many=True)
  return Response(serializer.data)

@api_view(['GET'])
def detail(request, pk):
  birthday = Birthday.objects.get(id=pk)
  serializer = BirthdaySerializer(birthday, many=False)
  return Response(serializer.data)


