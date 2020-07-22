from django import forms

from .models import Wpis

class PostForm(forms.ModelForm):
    class Meta:
        model = Wpis
        fields = ['strzelec', 'punkty', 'oddane_strzaly', 'dystans', 'published_date',  ]