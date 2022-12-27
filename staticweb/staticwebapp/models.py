from django.db import models


# Create your models here.
class Studend(models.Model):
    objects = None
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='pic')
    dcsrptn = models.TextField()

    def __str__(self):
        return self.name


class Studend1(models.Model):
    objects = None
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='pic')
    dcsrptn = models.TextField()

    def __str__(self):
        return self.name
