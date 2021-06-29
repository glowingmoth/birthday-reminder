from .models import Birthday
from django.utils import timezone
from django.shortcuts import render

def index(request):
  timeNow = timezone.now()
  context = {
    'object_list': Birthday.objects.all(),
    'object_this_month': Birthday.objects.filter(birthDate__month=timeNow.strftime('%m')),
    'timeNow': timeNow,
    'object_today': Birthday.objects.filter(birthDate__month=timeNow.strftime('%m'), birthDate__day=timeNow.strftime('%d'))
  }
  return render(request, 'birthdays/index.html', context)

  