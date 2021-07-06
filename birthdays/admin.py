from django.contrib import admin
from .models import Birthday

class BirthdayAdmin(admin.ModelAdmin):
  fields = [
    'firstName',
    'lastName',
    'birthDate',
    'created_at',
    'updated_at',
    'created_by',
  ]
  readonly_fields = ['created_at', 'updated_at']
  list_display = ('firstName', 'lastName', 'birthDate', 'created_at', 'updated_at','created_by')

  class Meta:
    model = Birthday

admin.site.register(Birthday, BirthdayAdmin)