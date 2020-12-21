from django.contrib import admin
from data_app.models import Folder
from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin

admin.site.register(Folder, DraggableMPTTAdmin)