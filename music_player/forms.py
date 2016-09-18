from django.forms import ModelForm
from django import forms 
from .models import *
from django.utils.text import slugify

class AddingMusicForm(ModelForm):
	class Meta:
		model = AddingMusicall 
		fields = ('origin','release_date',)
		initials = slugify('slug')

class AddingArtistForm(ModelForm):
	class Meta:
		model = Artist
		fields = '__all__'
		exclude = ('slug','artist_album_list',)
		prepopulated_fields = {'slug' : ('artist_name',)}

class PlaylistForm(ModelForm):
	class Meta:
		model = Playlist				
		fields = '__all__'
		exclude = ('slug',)