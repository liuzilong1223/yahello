from django.shortcuts import render
from hashlib import sha1
from models import *
from django.shortcuts import redirect
# Create your views here.

def register(request):
    return render(request, 'player/register.html')

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


def login(request):
    return render(request, 'player/login.html')