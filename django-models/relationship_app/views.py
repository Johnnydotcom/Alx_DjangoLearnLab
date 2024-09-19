
from django.shortcuts import render
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView
from django.views.generic import DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import user_passes_test



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
    return render(request, 'registration_app/register.html', {'form': form})

def is_admin(user):
    return user.is_authenticated and hasattr(user, 'profile') and user.profile.role == 'Admin'
def admin_view(request):
    return render(request, 'admin/dashboard.html')

def is_librarian(request):
    return user.is_authenticated and hasattr(user, 'profile') and user.profile.role == 'Librarian'
def librarian_view(request):
    return render(request, 'librarian/dashboard.html')

def is_member(request):
    return user.is_authenticated and hasattr(user, 'profile') and user.profile.role = 'Member'
def member_view(request):
    return render(request, 'member/dashboard.html')

