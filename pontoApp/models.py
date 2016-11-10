from django.db import models

# Create your models here.
class Book(models.Model):
	date = models.DateField(auto_now_add=True)
	time = models.DateTimeField(auto_now_add=True)