from django.db import models

# Create your models here.

class PlayerInfo(models.Model):
    pname = models.CharField(max_length=20)
    ppwd = models.CharField(max_length=40)
    pemail = models.CharField(max_length=20)
    pshou = models.CharField(max_length=10, default='')
    paddr = models.CharField(max_length=100, default='')
    pcode = models.CharField(max_length=6, default='')
    pphone = models.CharField(max_length=11, default='')
