from django import forms
from .models import Bookmark


class BookmarkForm(forms.ModelForm):
    class Meta:
        model = Bookmark
        fields = ['name', 'urlname', 'urlparams']
        widgets = {
            'urlname': forms.HiddenInput(),
            'urlparams': forms.HiddenInput(),
        }
