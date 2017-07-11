from django.db import models
from tinymce.models import HTMLField

# Create your models here.

class TypeInfo(models.Model):
    ttitle = models.CharField(max_length=20)
    tisDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.ttitle.encode('utf-8')


class GoodsInfo(models.Model):
    gtitle = models.CharField(max_length=20)
    gimages = models.ImageField(upload_to='goods')
    gprice = models.DecimalField(max_digits=6, decimal_places=2)
    gclick = models.IntegerField(default=0)
    gunit = models.CharField(max_length=20)
    gisDelete = models.BooleanField(default=False)
    gconcise = models.CharField(max_length=200)
    gstorage = models.IntegerField(default=100)
    gtype = models.ForeignKey('TypeInfo')
    gcontent = HTMLField()