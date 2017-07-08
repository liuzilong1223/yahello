from django.shortcuts import redirect

def player_login(func):
    def func1(request, *ages, **kwages):
        if request.session.has_key('uid'):
            return func(request, *ages, **kwages)
        else:
            return redirect('/player/login/')
    return func1
