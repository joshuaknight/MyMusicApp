from django.shortcuts import render
from .models import *
from .forms import *
from django.views.generic import *
from django.utils import timezone
from mymusic.settings import *
from django.core.urlresolvers import reverse

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
	context_object_name = 'album'

class MusicDetail(DetailView):
	template_name = 'album_detail.html'
	model = AddingMusicall
	context_object_name = 'album'
	slug_field = 'slug'


class Musicadd(View):
	def get(self, request):
		context = {
			'form' : AddingMusicForm,
			'key' : 'submit',
			'artist' : AddingArtistForm,
			'album' : PlaylistForm
		}
		return render(request,'form.html',context)

	def post(self, request):   
	    	user_form    = UserForm(prefix='user_form')
	        billing_form = BillingForm(prefix='billing_form')

	        # determine which form is submitting (based on hidden input called 'action')
	        action = self.request.POST['action']

	        # bind to POST and process the correct form
	        if (action == 'edit_user'):
	            user_form = UserForm(request.POST, prefix='user_form')
	            if user_form.is_valid():
	                form.save()
	        elif (action == 'edit_billing'):
	            billing_form = BillingForm(request.POST, prefix='billing_form')
	            if billing_form.is_valid():
	                pass

	def get_context_data(self,*args,**kwargs):
		context = super(Musicadd,self).get_context_data(*args,**kwargs)
		context['key'] = 'AddAlbum'
		return context

	def get_success_url(self):
		return reverse('add-music')		








class Artistdetail(DetailView):
	template_name = 'artist_detail.html'
	model = Artist
	context_object_name = 'artist'
	slug_field = 'slug'