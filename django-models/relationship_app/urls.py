from django.urls import path
from .views import list_books, LibraryDetailView, register
from . import views
from django.contrib.auth import views as auth_views
from .views import admin_view, librarian_view, member_view

urlpatterns = [
    path('relationship_app/', list_books, name='list_books'),
    path('relationship_app/', LibraryDetailView.as_view(), name='library_detail'),
    path('relationship_app/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('relationship_app/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('relationship_app/', views.register, name='register'),
    # path('relationship_app/', is__admin, name='is_admin'),
    # path('relationship_app/', is_librarian, name='is_librarian'),
    # path('relationship_app/', is_member, name='is_member'),
    path('admin/', admin_view, name='admin_view'),
    path('librarian/', librarian_view, name='librarian_view'),
    path('member/', member_view, name='member_view'),
    path('add_book/', add_book, name='add_book'),
    path('edit_book/', change_book, name='edit_book'),
    path('delete_book/', delete_book, name='delete_book'),
]
