from django import forms
from .models import Bookmark
from .settings import BOOKMARK_FORM_NAME


class BookmarkForm(forms.ModelForm):
    class Meta:
        model = Bookmark
        fields = ['name', 'urlname', 'urlparams']
        widgets = {
            'urlname': forms.HiddenInput(),
            'urlparams': forms.HiddenInput(),
        }
        labels = {
            'name': BOOKMARK_FORM_NAME,
        }
