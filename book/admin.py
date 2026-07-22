from django.contrib import admin

from book.models import BookGenre, Book

@admin.register(BookGenre)
class BookGenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'genre', 'was_loaned',)
    search_fields = ('name', 'author', 'genre__name',)
    list_filter = ('was_loaned',)
