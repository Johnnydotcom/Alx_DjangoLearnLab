from .models import Book
from .models import Librarian
from .models import Library, Author

library_name = ""
author_name = ""
author = ""
books_by_author = Author.objects.get(name=author_name).objects.filter(author=author)

books = Library.objects.get(name=library_name).books.all()
librarian = Librarian.objects.filter(library='idk')