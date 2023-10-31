from django.db import models
from django.contrib import admin
class Players(models.Model):
    pid=models.CharField(max_length=20,help_text="Player ID")
    name=models.CharField(max_length=100)
    team=models.CharField(max_length=50)
    age=models.IntegerField()
    rating=models.IntegerField()

class PlayerAdmin(admin.ModelAdmin):
    list_display=('pid','name','team','age','rating')