from django.urls import path
from .views import list_books, LibraryDetailView
from . import views

urlpatterns = [
    path('relationship_app/templates/', list_books, name='list_books'),
    path('relationship_app/templates/', LibraryDetailView.as_view(), name='library_detail'),
]
