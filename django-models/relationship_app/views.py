
from django.shortcuts import render, redirect
from .models import Book
from .models import Library
from .models import UserProfile
from django.views.generic.detail import DetailView
from django.views.generic import DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required


# Create your views here.
def list_books(request):
    books = Book.objects.all()
    context = {'list_books': books}
    return render(request, 'relationship_app/list_books.html', context)

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('relationship_app/register.html') 
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# def is_admin(user):
#     return user.is_authenticated and hasattr(user, 'profile') and user.profile.role == 'Admin'
# def is_librarian(user):
#     return user.is_authenticated and hasattr(user, 'profile') and user.profile.role == 'Librarian'
# def is_member(user):
#     return user.is_authenticated and hasattr(user, 'profile') and user.profile.role == 'Member'

# @login_required
# @user_passes_test(is_admin)
# def admin_view(request):
#     if request.user.is_authenticated and request.user.is_staff:
#         return render(request, 'relationship_app/admin.html')

# @login_required
# @user_passes_test(is_librarian)
# def librarian_view(request):
#     if request.user.is_authenticated and request.user.groups.filter(name='Librarians').exists():
#         return render(request, 'relationship_app/librarian.html')

# @login_required
# @user_passes_test(is_member)
# def member_view(request):
#     if request.user.is_authenticated and request.user.groups.filter(name='Member').exists():
#         return render(request, 'relationship_app/member.html')

def is_admin(user):
    #return user.is_authenticated and user.groups.filter(name='Admin').exists()
    return user.is_authenticated and user.userprofile.role == 'Admin'

def is_librarian(user):
   # return user.is_authenticated and user.groups.filter(name='Librarian').exists()
   return user.is_authenticated and user.userprofile.role == 'Librarian'

def is_member(user):
   # return user.is_authenticated and user.groups.filter(name='Member').exists()
   return user.is_authenticated and user.userprofile.role == 'Member'

# Admin View
@login_required

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'admin.html')  # Admin-specific content

# Librarian View
@login_required

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'librarian.html')  # Librarian-specific content

# Member View
@login_required

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'member.html')

@permission_required('relationship_app.can_add_book')
def add_book(request):
    if request.method == "POST":
        title = request.POST['title']
        author = request.POST['author']
        Book.objects.create(title=title, author=author)
        return redirect('book_list')  # Replace with your actual book list view
    return render(request, 'add_book.html')

@permission_required('relationship_app.can_change_book')
def change_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        book.title = request.POST['title']
        book.author = request.POST['author']
        book.save()
        return redirect('book_list')  # Replace with your actual book list view
    return render(request, 'change_book.html', {'book': book})

@permission_required('relationship_app.can_delete_book')
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        book.delete()
        return redirect('book_list')  # Replace with your actual book list view
    return render(request, 'delete_book.html', {'book': book})