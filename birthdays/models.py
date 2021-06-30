from django.db import models
from django.db.models.fields import CharField

class Birthday(models.Model):
  firstName = models.CharField(max_length=30, blank=False, null=False)
  lastName = models.CharField(max_length=30, blank=False, null=False)
  birthDate = models.DateField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return f'{self.firstName} {self.lastName}' 


