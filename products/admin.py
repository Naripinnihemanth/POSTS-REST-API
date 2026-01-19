from django.contrib import admin
from .models import *

class postAdmin(admin.ModelAdmin):
    list_display=("id","post_title")

admin.site.register(postModel,postAdmin)