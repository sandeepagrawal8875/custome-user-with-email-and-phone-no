from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from .forms import CustomUserCreationForm


def signup(request):
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'signup.html', {'form': form})


@login_required(login_url='login')
def home(request):
    return render(request, 'home.html')

@login_required(login_url='login')
def logoutview(request):
    logout(request)
    return redirect('login')