from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


# views.py


def home_view(request):
    return render(request, 'home.html')


def connexion_view(request):
    return render(request, 'connexion.html')

def inscription_view(request):
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('blogapp:home')
        
    else:
        form = UserCreationForm()
    return render(request, 'inscription.html', {'form': form})