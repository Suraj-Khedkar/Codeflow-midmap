from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^newevent/$', views.new_event, name='new_event'),
    url(r'^profile/$', views.profile, name='profile'),
]
