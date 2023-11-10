from django.contrib.gis.db import models

# Create your models here.
class Shop(models.Model):
    name=models.CharField(max_length=100)
    location=models.PointField()
    address=models.CharField(max_length=200)
    city=models.CharField(max_length=50)

    def __str__(self):
        return self.name