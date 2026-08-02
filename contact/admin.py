from django.contrib import admin

from contact import models


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    pass
list_display = 'first_name', 'last_name', 'phone',
ordering = 'id', 'first_name', 'last_name',