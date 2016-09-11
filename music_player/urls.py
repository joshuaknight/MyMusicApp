from django.conf.urls import url
from .views import *

urlpatterns = [
	url(r'^home$',home.as_view(),name = 'home'),
	url(r'^add$',AddingMusic.as_view(),name = 'album'),
]

