from django.contrib import admin
from .models import Page

# Register your models here.
class pageAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

admin.site.register(Page, pageAdmin)


