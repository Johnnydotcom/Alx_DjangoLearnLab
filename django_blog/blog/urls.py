from django.urls import path
from . import views
from .views import login_view, logout_view, register_view, profile_view, PostListView, PostCreateView, PostUpdateView, PostDeleteView, CommentUpdateView, CommentDeleteView

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('profile/', views.profile_view(), name='profile'),
    path('post/', PostListView.as_view(), name='list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='view'),
    path('post/new/', PostCreateView.as_view(), name='create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='edit'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='delete'),
    path('comment/<int:pk>/new/', CommentCreateView.as_view(), name='comment-create'),
    path('comment/<int:pk>/edit/', CommentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
]