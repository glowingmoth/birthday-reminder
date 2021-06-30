from datetime import datetime
from .models import Birthday
from django.utils import timezone
import datetime
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def index(request):
  testDate = datetime.datetime(1998, 1, 14)
  
  # timeNow = testDate
  timeNow = timezone.localtime()
 
  context = {
    'timeNow': timeNow,
    'object_list': Birthday.objects.all(),
    'object_this_month': Birthday.objects.filter(birthDate__month=timeNow.strftime('%m')),
    'object_this_week': Birthday.objects.filter(birthDate__week=timeNow.strftime('%W')),
    'object_today': Birthday.objects.filter(birthDate__day=timeNow.strftime('%d'))
  }
  print(context['object_this_month'])
  return render(request, 'birthdays/index.html', context)

def addBirthday(request):
  return render(request, 'birthdays/addbirthday.html' )

# There was some bug/issue with using 'timezone.now()' so I changed it to 'timezone.localtime()' and that resolved it.
# The problem was .now() returns the current UTC and not the local time adjusted.
  