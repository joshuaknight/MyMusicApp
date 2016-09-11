from __future__ import unicode_literals

from django.db import models



class Album(models.Model):
	artist = models.CharField(max_length = 200)


	def __str__(self):
		return self.artist

class AddingMusicall(models.Model):
	artist_name_key = models.ForeignKey("Album")
	album_name_key = models.ForeignKey("Music_list")
	slug = models.SlugField()
	#photo = models.ImageField(upload_to = 'album/photos')
	artist_name = models.CharField(max_length = 200)
	album_name = models.CharField(max_length = 200)
	origin = models.CharField(max_length = 200)
	release_date = models.DateField()

	def __str__(self):
		return self.artist_name
	

class Music_list(models.Model):
	music_list = models.CharField(max_length=200)	
	num1 = models.CharField(max_length = 100,blank = True)
	num2 = models.CharField(max_length = 100,blank = True)
	num3 = models.CharField(max_length = 100,blank = True)
	num4 = models.CharField(max_length = 100,blank = True)
	num5 = models.CharField(max_length = 100,blank = True)
	num6 = models.CharField(max_length = 100,blank = True)
	num7 = models.CharField(max_length = 100,blank = True)
	num8 = models.CharField(max_length = 100,blank = True)
	num9 = models.CharField(max_length = 100,blank = True)
	num10 = models.CharField(max_length = 100,blank = True)
	num11 = models.CharField(max_length = 100,blank = True)
	num12 = models.CharField(max_length = 100,blank = True)
	num13 = models.CharField(max_length = 100,blank = True)
	num14 = models.CharField(max_length = 100,blank = True)
	num15 = models.CharField(max_length = 100,blank = True)

	def __str__(self):
		return self.music_list