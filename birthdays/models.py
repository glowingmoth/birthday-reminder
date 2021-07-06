from django.db import models
from django.db.models.fields import CharField
from django.contrib.auth.models import User
from django.urls import reverse

class Birthday(models.Model):
  firstName = models.CharField(max_length=30, blank=False, null=False)
  lastName = models.CharField(max_length=30, blank=False, null=False)
  birthDate = models.DateField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  created_by= models.ForeignKey(User, null=True,on_delete=models.CASCADE)

  def __str__(self):
    return f'{self.firstName} {self.lastName}' 

  @property
  def get_update_url(self):
    return reverse('updateBirthday', kwargs={'pk':self.id} )
