from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    """ Contact Table """

    list_display = (
        'name',
        'email',
        'order_number',
        'message',
        'date'
    )
    search_fields = ('name', 'email',)
    date_hierarchy = 'date'

admin.site.register(Contact, ContactAdmin)
