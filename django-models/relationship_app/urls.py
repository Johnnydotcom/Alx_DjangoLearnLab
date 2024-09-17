from django.urls import path
from .views import list_books, LibraryDetailView
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('relationship_app/', list_books, name='list_books'),
    path('relationship_app/', LibraryDetailView.as_view(), name='library_detail'),
    path('relationship_app/', auth_views.LogoutView.as_view(template_name='registration_app/logout.html'), name='logout'),
    path('relationship_app/', auth_views.LoginView.as_view(template_name='registration_app/login.html'), name='login'),
    path('relationship_app/', register, name='register'),
]
