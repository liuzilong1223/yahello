from django.conf.urls import url
import views

urlpatterns = [
    url(r'^register/$', views.register),
    url(r'^player_zc/$', views.player_zc),
    url(r'^player_name/$', views.player_name),
    url(r'^login/$', views.login),
    url(r'^login_yz/$', views.login_yz),
    url(r'^login_out/$', views.login_out),
    url(r'^$', views.center),
    url(r'^order/$', views.order),
    url(r'^site/$', views.site),
    url(r'^islogin/$', views.islogin),
]