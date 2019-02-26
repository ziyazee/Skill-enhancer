from django.db import models

class CodingSets(models.Model):
    Title=models.CharField(max_length=500,unique=True)
    Description=models.CharField(max_length=50000,unique=True)
