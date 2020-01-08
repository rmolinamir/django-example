from django.contrib import admin
from .models import Book, BookGenre

admin.site.register(Book)
admin.site.register(BookGenre)
