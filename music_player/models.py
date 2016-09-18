from __future__ import unicode_literals

from django.db import models


def get_album_name(instance,filename):
	try:
		x = AddingMusicall.objects.all().__len__()		
		a = AddingMusicall.objects.get(pk = x)		
		return "songs/%s/%s"%(a.album_name,filename)
	except:
		album_name = 'Album1'
		return "songs/%s"%(album_name)		

class Playlist(models.Model):
	album_name = models.CharField(max_length=200,unique  = True)	
	album_photo = models.ImageField(upload_to = 'album/photos')
	slug = models.SlugField()
	song1 =  models.FileField(upload_to = get_album_name,blank = True)
	song2 =  models.FileField(upload_to = get_album_name,blank = True)
	song3 =  models.FileField(upload_to = get_album_name,blank = True)
	song4 =  models.FileField(upload_to = get_album_name,blank = True)
	song5 =  models.FileField(upload_to = get_album_name,blank = True)
	song6 =  models.FileField(upload_to = get_album_name,blank = True)
	song7 =  models.FileField(upload_to = get_album_name,blank = True)
	song8 =  models.FileField(upload_to = get_album_name,blank = True)
	song9 =  models.FileField(upload_to = get_album_name,blank = True)
	song10 =  models.FileField(upload_to = get_album_name,blank = True)
	song11 =  models.FileField(upload_to = get_album_name,blank = True)
	song12 =  models.FileField(upload_to = get_album_name,blank = True)
	song13 =  models.FileField(upload_to = get_album_name,blank = True)
	song14 =  models.FileField(upload_to = get_album_name,blank = True)
	song15 =  models.FileField(upload_to = get_album_name,blank = True)


	def save(self,*args,**kwargs):
		self.slug = self.album_name
		return self.slug.save()

	def __str__(self):
		return self.album_name

class Artist(models.Model):
	artist_name = models.CharField(max_length = 200,unique = True)
	artist_place = models.CharField(max_length = 200)
	artist_date = models.DateField(blank = True)
	artist_album_list = models.ManyToManyField(Playlist,blank = True)
	slug = models.SlugField()
	artist_photo = models.ImageField(upload_to = 'artist/photos')

	def __str__(self):
		return self.artist_name

class AddingMusicall(models.Model):
	artist = models.ForeignKey("Artist")
	album = models.ForeignKey("Playlist")
	slug = models.SlugField()			
	origin = models.CharField(max_length = 200)
	release_date = models.DateField()	
	
	

	def __str__(self):
		return self.slug
	

