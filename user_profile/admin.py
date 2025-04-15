from django.contrib import admin
from .models import UserData

@admin.register(UserData)
class UserDataAdmin(admin.ModelAdmin):
    list_display = ('name', 'student_id', 'birthdate', 'birth_time', 'city', 'town')
    search_fields = ('name', 'student_id')
    list_filter = ('city',)
