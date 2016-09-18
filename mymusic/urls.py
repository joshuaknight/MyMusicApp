from django.conf.urls import url,include
from django.contrib import admin
from music_player.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls), 
    url(r'^music/',include('music_player.urls')),
    url(r'^$', home.as_view(),name='home'), 
]
