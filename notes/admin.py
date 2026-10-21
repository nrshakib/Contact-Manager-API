from django.contrib import admin

from notes.models import Notes

# Register your models here.
@admin.register(Notes)
class NotesAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'content', 'priority', 'created_at' ]
    search_fields = ['title']
    list_filter = ['category', 'priority']