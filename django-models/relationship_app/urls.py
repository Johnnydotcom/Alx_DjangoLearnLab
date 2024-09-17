from django.urls import path
from .views import list_books, LibraryDetailView, register
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('relationship_app/', list_books, name='list_books'),
    path('relationship_app/', LibraryDetailView.as_view(), name='library_detail'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout/logout.html'), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='login/login.html'), name='login'),
    path('register/', views.register, name='register'),
]
