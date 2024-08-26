book = Book.objects.get(title='1984')

book.publication_year = 'Nineteen Eighty-Four'
book.save()