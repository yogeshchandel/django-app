from django.contrib import admin
from .models import Book

# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'published_date', 'isbn_number')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'author__name', 'isbn_number')
    list_filter = ('published_date',)
    list_per_page = 25