  
from django import forms
from data_app.models import Folder


class NewFolderForm(forms.Form):
    # class Meta:
    #     model = Folder
    #     fields = ('name', 'parent')
    #     widgets = {
    #         'name': forms.TextInput(attrs={'class': 'col-sm-12'}),
    #         'parent': forms.TextInput(attrs={'class': 'col-sm-12'}),
    #  

    name = forms.CharField(max_length=100)
    parent = forms.ModelChoiceField(queryset=Folder.objects.all())