from django.contrib import admin
from .models import Note

# Register your models here.


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_by', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'created_by')
    search_fields = ('title', 'body')
    # prepopulated_fields = {('title',)}
    raw_id_fields = ('created_by',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')
