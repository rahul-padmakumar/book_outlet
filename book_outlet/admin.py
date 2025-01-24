from django.contrib import admin

# Register your models here.
from .models import Book

class BookAdmin(admin.ModelAdmin):
    readonly_fields = ("slug",)

admin.site.register(Book, BookAdmin)
