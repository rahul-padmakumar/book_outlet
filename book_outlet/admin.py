from django.contrib import admin

# Register your models here.
from .models import Book

class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("title",)}

admin.site.register(Book, BookAdmin)
