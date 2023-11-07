from django.db import models


# Create your models here.
class Casestudy1(models.Model):
    Name = models.CharField(max_length=200)
    Image = models.ImageField(upload_to="Pictures")
    Desc = models.TextField()
    def __str__(self):
        return self.Name

class Services(models.Model):
    Name1 = models.CharField(max_length=200)
    Image1 = models.ImageField(upload_to="Pictures1")
    Desc1 = models.TextField()
    More = models.CharField(max_length=200)
    def __str__(self):
        return self.Name1
