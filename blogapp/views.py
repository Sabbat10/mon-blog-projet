from django.shortcuts import render

# views.py


def home_view(request):
    return render(request, 'home.html')


def connexion_view(request):
    return render(request, 'connexion.html')

def inscription_view(request):
    return render(request, 'inscription.html')