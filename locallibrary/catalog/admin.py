from django.contrib import admin

#Added imports
from .models import Book, Genre, BookInstance, Author

# Register your models here.
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(BookInstance)