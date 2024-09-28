from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('profile/', views.profile_view(), name='profile'),
    path('blog', PostListView.as_view(), name='list'),
    path('blog', PostDetailView.as_view(), name='detail'),
    path('blog', PostCreateView.as_view(), name='create'),
    path('blog', PostUpdateView.as_view(), name='update'),
    path('blog/', PostDeleteView.as_view(), name='delete')
]