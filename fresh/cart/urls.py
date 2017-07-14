from django.conf.urls import url
import views

urlpatterns = [
    url(r'^add/$', views.add),
    url(r'^count/$', views.count),
    url(r'^$', views.index),
    url(r'^edit/$', views.edit),
    url(r'^delete/$', views.delete),
    url(r'^order/$', views.order),
]