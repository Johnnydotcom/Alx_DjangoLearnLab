from django.shortcuts import render
from django.views.generic import DeleteView, DetailView, CreateView, UpdateView

# Create your views here.
def login_view(request):
    return render(request, 'login.html')

def logout_view(request):
    return render(request, 'logout.html')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('blog/register.html') 
    else:
        form = UserCreationForm()
    return render(request, 'blog/register.html', {'form': form})

def profile_view(request):
    return render(request, 'profile.html')

class PostUpdateView(UpdateView):
    model = Post
    template_name = 'update.html' 
    fields = ['title', 'content']
    
class PostCreateView(CreateView):
    model = Post
    template_name = 'create.html'   # Template for creating a post
    fields = ['title', 'content']
    
class PostDetailView(DetailView):
    model = Post
    template_name = 'detail.html'  # Template for a single post
    context_object_name = 'post'
    
class PostDeleteView(DeleteView):
    model = Post
    template_name = 'delete.html'  # Template for delete confirmation
    success_url = reverse_lazy('post-list')