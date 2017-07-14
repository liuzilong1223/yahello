from django.db import models

# Create your models here.

class OrderMain(models.Model):
    order_id = models.CharField(max_length=20, primary_key=True)
    player = models.ForeignKey('player.PlayerInfo')
    order_date = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=8, decimal_places=2)
    state = models.IntegerField()

class OrderDetail(models.Model):
    order = models.ForeignKey(OrderMain)
    goods = models.ForeignKey('commodity.GoodsInfo')
    count = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
