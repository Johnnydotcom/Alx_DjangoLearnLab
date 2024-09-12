
from django.shortcuts import render
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView
from django.views.generic import DetailView


# Create your views here.
def list_books(request):
    books = Book.objects.all()
    context = {'list_books': books}
    return render(request, 'templates/list_books.html', context)

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'templates/library_detail.html'
    context_object_name = 'library'

    

