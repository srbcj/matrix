# coding:utf-8

from django.contrib import admin
from inventory.models import Inventory,Contact,Tag


# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    fieldsets = (
        ['Main',{
            'fields':('name','email'),
        }],
        ['Advance',{
            'classes': ('collapse',), # CSS
            'fields': ('age',),
        }]
    )
    search_fields = ('name',)


admin.site.register(Contact, ContactAdmin)

# Register your models here.
admin.site.register([Inventory, Tag])