from django.db import models

# Create your models here.

class CartInfo(models.Model):
    player = models.ForeignKey('player.PlayerInfo')
    goods = models.ForeignKey('commodity.GoodsInfo')
    count = models.IntegerField()