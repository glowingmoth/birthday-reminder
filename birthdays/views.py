from .models import Birthday
from django.utils import timezone
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def index(request):
  timeNow = timezone.now()
  context = {
    'timeNow': timeNow,
    'object_list': Birthday.objects.all(),
    'object_this_month': Birthday.objects.filter(birthDate__month=timeNow.strftime('%m')),
    'object_this_week': Birthday.objects.filter(birthDate__month=timeNow.strftime('%m'), birthDate__week=timeNow.strftime('%W')),
    'object_today': Birthday.objects.filter(birthDate__month=timeNow.strftime('%m'), birthDate__day=timeNow.strftime('%d'))
  }
  return render(request, 'birthdays/index.html', context)


# The Query Set field lookup '__day' only takes integers however .strftime() 2nd argument '%d' uses decimals which caused a bug
# when displaying birthdays for the current day. Converting the formatted number to an integer fixed the bug. 
  