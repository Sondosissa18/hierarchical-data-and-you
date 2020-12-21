  
from django import forms
from data_app.models import Folder


class NewFolderForm(forms.Form):
    name = forms.CharField(max_length=100)
    parent = forms.ModelChoiceField(queryset=Folder.objects.all())