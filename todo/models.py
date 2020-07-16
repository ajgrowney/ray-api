from django.db import models

# Create your models here.
class Reminder(models.Model):
	text=models.CharField(max_length=128)
	priority=models.IntegerField(default=-1)
	time=models.DateTimeField(null=True, blank=True)

class Chore(models.Model):
	text=models.CharField(max_length=128)
	