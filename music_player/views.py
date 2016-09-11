from django.shortcuts import render
from .models import *
from .forms import *
from django.views.generic import *
from django.utils import timezone
from mymusic.settings import *

# Create your views here.
class home(TemplateView):
	template_name = 'index.html'
	
	def get_context_data(self,*args,**kwargs):
		context = super(home,self).get_context_data(*args,**kwargs)
		context['time'] = timezone.now()
		return context 
	

class AddingMusic(ListView):
	template_name = 'album_list.html'
	model  = AddingMusicall


print BASE_DIR