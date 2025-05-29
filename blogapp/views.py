from django.shortcuts import render

# views.py


def home_view(request):
    return render(request, 'home.html')