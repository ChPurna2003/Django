from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import views as auth_views

# User Registration View
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('chat:room', room_name='general')  # Redirect to a default chat room
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

# User Login View
def login_view(request):
    return auth_views.LoginView.as_view()(request)