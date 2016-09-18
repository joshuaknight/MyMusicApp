from django.contrib import admin
from .models import *
# Register your models here.
#class AddingMusicAdmin(admin.ModelAdmin):
#	prepopulated_fields = {'slug' : ('artist_name',)}



admin.site.register(Artist)
admin.site.register(Playlist)
admin.site.register(AddingMusicall)#,AddingMusicAdmin)

