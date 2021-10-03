from django.contrib import admin
from .models import *

# Register your models here.

from tinymce.widgets import TinyMCE

class EsotericAdmin(admin.ModelAdmin):

    formfield_overrides = {
        models.TextField : { 'widget' : TinyMCE()}
    }

admin.site.register(Book)
admin.site.register(Blog, EsotericAdmin)
admin.site.register(Subscription)
