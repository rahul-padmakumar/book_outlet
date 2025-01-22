from django.shortcuts import render
from book_outlet.models import Book
from django.http import Http404, HttpResponseNotFound
from django.template.loader import render_to_string

# Create your views here.

def index(request):
    books = Book.objects.all()
    return render(request, "book_outlet/index.html", {"books": books})

def details(request, id):
    try:
        book = Book.objects.filter(id=id)[0]
    except:
        return HttpResponseNotFound(render_to_string("404.html"))
    return render(request, "book_outlet/details.html", {"title": book.title, "author": book.author, "is_bestseller": book.is_bestselling})
