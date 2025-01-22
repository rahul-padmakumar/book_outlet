from django.shortcuts import render
from book_outlet.models import Book
from django.http import Http404, HttpResponseNotFound
from django.template.loader import render_to_string
from django.shortcuts import get_object_or_404

# Create your views here.

def index(request):
    books = Book.objects.all()
    return render(request, "book_outlet/index.html", {"books": books})

def details(request, id):
    book = get_object_or_404(Book, id=id)
    return render(request, "book_outlet/details.html", {"title": book.title, "author": book.author, "is_bestseller": book.is_bestselling})
