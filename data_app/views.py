from django.shortcuts import render, HttpResponseRedirect, reverse
from .forms import NewFolderForm
from django.views.generic import ListView
from data_app.models import Folder

def index(request):

    all_folders = Folder.objects.all()

    return render(request, 'home.html', {'folder': all_folders})

   



def create_folder(request):
    html = "generic_form.html"
    if request.user.is_staff:
        if request.method == "POST":
            form = NewFolderForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                Folder.objects.create(
                    name = data['name'],
                    parent = data['parent'],
                )
                return HttpResponseRedirect(reverse("homepage"))
    form = NewFolderForm()
    return render(request, html, {"form": form})


