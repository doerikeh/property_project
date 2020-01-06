from django.contrib import admin

from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'is_published', 'price', 'list_update', 'realtor']
    list_display_links = ('id', 'title')
    list_filter = ('realtor',)
    list_editable = ('is_published',)
    search_fields = ('title', 'realtor', 'description', 'address', 'zip', 'state')
    list_per_page = 20

admin.site.register(Listing, ListingAdmin)