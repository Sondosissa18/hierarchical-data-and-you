from django.shortcuts import render, HttpResponseRedirect, reverse
from .forms import NewFolderForm
from django.views.generic import ListView
from data_app.models import Folder

def index(request):

    all_folders = Folder.objects.all()

    return render(request, 'home.html', {'folder': all_folders})

    # item.get_ancestors()



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


# def create_folder(request):
#     if request.method == 'POST':
#         folder_form = NewFolderForm(request.POST)
#         if folder_form.is_valid():
#             folder_form = folder_form.save(commit=False)
#             folder_form.post = post
#             folder_form.save()
#             return HttpResponseRedirect('home')
#     else:
#         folder_form = NewFolderForm()
#     return render(request, 'folder.html', {'folder_form': folder_form})


