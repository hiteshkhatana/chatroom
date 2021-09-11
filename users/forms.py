from django import forms
from django.db import models
from django import forms
from .models import ProfileModel

class ImageForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = ['dp']
