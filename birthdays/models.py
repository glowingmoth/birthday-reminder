from django.db import models
from django.db.models.fields import CharField

class Birthday(models.Model):
  first_name = models.CharField(max_length=30, blank=False, null=False)
  last_name = models.CharField(max_length=30, blank=False, null=False)
  birth_date = models.DateField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.first_name


