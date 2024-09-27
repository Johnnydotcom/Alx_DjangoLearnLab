from django.shortcuts import render

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