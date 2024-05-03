from django.db import models

# Create your models here.
class personne(models.Model):
	username = models.fields.CharField(max_length=200)
	password = models.fields.CharField(max_length=200)

