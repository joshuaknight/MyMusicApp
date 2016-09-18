from django.conf.urls import url
from .views import *

urlpatterns = [
	url(r'^home$',home.as_view(),name = 'home'),
	url(r'^list$',AddingMusic.as_view(),name = 'album'),
	url(r'^detail/(?P<slug>[\w-]+)/*$',MusicDetail.as_view(),name = 'album-detail'),
	url(r'^artist/(?P<slug>[\w-]+)/*$',Artistdetail.as_view(),name = 'artist-detail'),
	url(r'^add$',Musicadd.as_view(),name = 'add-music')
]

