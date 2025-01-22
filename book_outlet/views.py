from django.shortcuts import render
from book_outlet.models import Book
from django.http import Http404, HttpResponseNotFound
from django.template.loader import render_to_string
from django.shortcuts import get_object_or_404
from django.db.models import Max, Avg

# Create your views here.

def index(request):
    books = Book.objects.all().order_by("-author")
    for book in books:
        print(book.rating)
    print(books.count())
    print(books.aggregate(Max("rating"))["rating__max"])
    print(books.aggregate(Avg("rating"))["rating__avg"])
    return render(request, "book_outlet/index.html", {"books": books})

def details(request, slug):
    book = get_object_or_404(Book, slug=slug)
    return render(request, "book_outlet/details.html", {"title": book.title, "author": book.author, "is_bestseller": book.is_bestselling})
