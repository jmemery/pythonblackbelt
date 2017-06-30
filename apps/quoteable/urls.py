from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.index, name='loginandres'),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^home$', views.home, name="home"),
    url(r'^addquote$', views.addquote),
    url(r'^mylikes$', views.mylikes,name="user"),
    url(r'^likequote/(?P<quoteid>\d+)$', views.likequote),
    #url(r'^user/(?P<user>\S+)$', views.user),
    url(r'^user/name$', views.username),
    url(r'^delete$', views.delete),
    ]
