from django.forms import ModelForm
from django import forms 
from .models import *

class AddingMusicForm(ModelForm):
	class Meta:
		model = AddingMusicall
		fields = '__all__'