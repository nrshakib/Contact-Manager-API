from django.contrib import admin
from contact.models import Contact

# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'phone', 'company']
    search_fields = ['name', 'email']
    list_filter = ['created_at']