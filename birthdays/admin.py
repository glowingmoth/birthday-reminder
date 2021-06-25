from django.contrib import admin
from .models import Birthday

class BirthdayAdmin(admin.ModelAdmin):
  fields = [
    'firstname',
    'last_name',
    'birth_date',
    'created_at',
    'updated_at',
  ]
  readonly_fields = ['created_at', 'updated_at']
  list_display = ('first_name', 'last_name', 'birth_date', 'created_at', 'updated_at')

  class Meta:
    model = Birthday

admin.site.register(Birthday, BirthdayAdmin)