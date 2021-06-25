from .models import Birthday
from django.utils import timezone
from django.shortcuts import render

def index(request):
  now = timezone.now()
  context = {
    'object_list': Birthday.objects.all(),
    'object_list_thisMonth': Birthday.objects.filter(birth_date__month=now.strftime('%m')),
     'now': now,
     'object_today': Birthday.objects.filter(birth_date__month=now.strftime('%m'), birth_date__day=now.strftime('%d'))
     }
  return render(request, 'birthdays/index.html', context)
