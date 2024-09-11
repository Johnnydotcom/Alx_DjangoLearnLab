from .models import Book
from .models import Librarian
from .models import Library

library_name = ""

books_by_author = Book.objects.filter(author='John Doe')

books = Library.objects.get(name=library_name).books.all()
librarian = Librarian.objects.filter(library='idk')