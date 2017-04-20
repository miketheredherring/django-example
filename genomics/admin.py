from django.contrib import admin

from genomics.models import Disease, Gene


# Register your models here.
admin.site.register(Disease)
admin.site.register(Gene)
