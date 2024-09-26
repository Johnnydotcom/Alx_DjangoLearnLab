from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.hello_view, name='login'),
    path('logout/', views.AboutView.as_view(), name='logout'),
    path('register/', views.hello_view, name='register'),
    path('profile/', views.AboutView.as_view(), name='profile'),
]