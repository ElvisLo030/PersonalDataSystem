from django.db import models

# Create your models here.

class UserData(models.Model):
    name = models.CharField(max_length=50, verbose_name='姓名')
    student_id = models.CharField(max_length=8, primary_key=True, verbose_name='學號')
    birthdate = models.DateField(verbose_name='生日')
    birth_time = models.TimeField(verbose_name='出生時間')
    city = models.CharField(max_length=50, verbose_name='縣市')
    town = models.CharField(max_length=50, verbose_name='鄉鎮')
    goal = models.TextField(max_length=255, verbose_name='追求目標')

    def __str__(self):
        return f"{self.name} ({self.student_id})"
