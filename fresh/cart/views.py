#coding=utf-8
from django.shortcuts import render
from django.shortcuts import render
from models import *
from django.http import JsonResponse
from django.db.models import Sum
from player.player_decorator import player_login
from player.models import PlayerInfo

# Create your views here.

def add(request):
    try:
        uid = request.session.get('uid')
        gid = int(request.GET.get('gid'))
        count = int(request.GET.get('count', '1'))

        carts = CartInfo.objects.filter(player_id=uid, goods_id=gid)
        if len(carts) == 1:
            cart = carts[0]
            cart.count += count
            cart.save()
        else:
            cart = CartInfo()
            cart.player_id = uid
            cart.goods_id = gid
            cart.count = count
            cart.save()
        return JsonResponse({'isadd': 1})
    except:
        return JsonResponse({'isadd': 0})

def count(request):
    uid = request.session.get('uid')
    # cart_count=CartInfo.objects.filter(user_id=uid).count()
    cart_count = CartInfo.objects.aggregate(Sum('count')).get('count__sum')
    return JsonResponse({'cart_count':cart_count})

@player_login
def index(request):
    uid = request.session.get('uid')
    cart_list = CartInfo.objects.filter(player_id=uid)
    context = {'title':'购物车', 'cart_list':cart_list}
    return render(request, 'cart/cart.html', context)

def edit(request):
    id = int(request.GET.get('id'))
    count = int(request.GET.get('count'))
    cart = CartInfo.objects.get(pk=id)
    cart.count = count
    cart.save()
    return JsonResponse({'ok':1})

def delete(request):
    id = request.GET.get('id')
    cart = CartInfo.objects.get(pk=id)
    cart.delete()
    return JsonResponse({'ok':1})

def order(request):
    id = PlayerInfo.objects.get(pk=request.session.get('uid'))
    cart_id = request.POST.getlist('cart_id')
    cart_list = CartInfo.objects.filter(id__in=cart_id)
    context = {'title':'提交订单', 'id':id, 'cart_list':cart_list}
    return render(request, 'cart/order.html', context)