from django.db import models

# Create your models here.

class Grocery(models.Model):
	item=models.CharField(max_length=64)
	
