#coding:utf-8
from django.shortcuts import render,redirect
from hashlib import sha1
from models import *
from django.http import JsonResponse
import datetime
from player_decorator import player_login
# Create your views here.

def register(request):
    context = {'title':'注册', 'top':'0'}
    return render(request, 'player/register.html', context)

def player_zc(request):
    post = request.POST
    name = post.get('user_name')
    pwd = post.get('pwd')
    email = post.get('email')

    s1 = sha1()
    s1.update(pwd)
    pwd_sha1 = s1.hexdigest()

    player = PlayerInfo()
    player.pname = name
    player.ppwd = pwd_sha1
    player.pemail = email
    player.save()
    return redirect('/player/login/')

def player_name(request):
    name = request.GET.get('name')
    result = PlayerInfo.objects.filter(pname=name).count()
    context = {'result':result}
    return JsonResponse(context)

def login(request):
    name = request.COOKIES.get('name', '')
    context = {'title':'登陆', 'top':'0', 'name':name}
    return render(request, 'player/login.html', context)

def login_yz(request):
    post = request.POST
    name = post.get('user_name')
    pwd = post.get('pwd')
    user_jz = post.get('user_jz','0')

    s1 = sha1()
    s1.update(pwd)
    pwd_sha1 = s1.hexdigest()

    player = PlayerInfo.objects.filter(pname=name)
    context = {'title':'登陆', 'top':'0'}
    if len(player) == 0:
        context['error_name'] = '1'
        return render(request, 'player/login.html', context)
    else:
        if player[0].ppwd == pwd_sha1:
            request.session['uid'] = player[0].id
            request.session['name'] = name
            response = redirect('/player/')
            if user_jz == '1':
                response.set_cookie('name', name, expires=datetime.datetime.now() + datetime.timedelta(days = 7))
            else:
                response.set_cookie('name', '', max_age=-1)
            return response
        else:
            context['error_pwd'] = '1'
            return render(request, 'player/login.html', context)

@player_login
def center(request):
    player = PlayerInfo.objects.get(pk=request.session['uid'])
    context = {'title':'用户中心', 'player':player}
    return render(request, 'player/center.html', context)

@player_login
def order(request):
    return render(request, 'player/order.html')

@player_login
def site(request):
    player = PlayerInfo.objects.get(pk=request.session['uid'])
    if request.method == 'POST':
        post = request.POST
        player.pshou = post.get('show')
        player.paddr = post.get('addr')
        player.pcode = post.get('code')
        player.pphone = post.get('phone')
        player.save()
    context = {'title':'收货地址', 'player':player}

    return render(request, 'player/site.html', context)