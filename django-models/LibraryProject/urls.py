"""
URL configuration for LibraryProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('relationship_app/', views.book_list, name = 'list_books'),
    # path('relationship_app/', views.BookDetailView.as_view(), name = 'library_detail'),
    # path('relationship_app/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    # path('relationship_app/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    # path('relationship_app/', views.register, name='register'),
    path('librarian/', librarian_view, name='librarian_view'),
    path('member/', member_view, name='member_view'),
    path('', include('relationship_app.urls')),
]
