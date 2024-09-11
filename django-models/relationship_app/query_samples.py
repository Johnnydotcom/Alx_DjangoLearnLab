from .models import Book
from .models import Librarian
from .models import Library



books_by_author = Book.objects.filter(author='John Doe')

books = Book.objects.all()
librarian = Librarian.objects.filter(library='idk')