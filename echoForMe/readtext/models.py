from django.db import models

# Create your models here.

class News(models.Model):
	id = models.AutoField(primary_key= True)
	newsHeading = models.CharField(max_length = 1000)
	newsContent = models.CharField(max_length = 10000)

class UserText(models.Model):
	id = models.AutoField(primary_key= True)
	text = models.CharField(max_length = 5000)