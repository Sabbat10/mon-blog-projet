from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout

from blogapp.forms import ArticleForms
from blogapp.models import Article


# views.py

# home view
def home_view(request):
    articles = Article.objects.all().order_by('-created_at')
    context = {
        'articles': articles,
    }
    return render(request, 'home.html', context)

def connexion_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('blogapp:home')
    else:
        form = AuthenticationForm()
    return render(request, 'connexion.html', {'form': form})

# inscription view
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


# logout view
def deconnexion_view(request):
    
    logout(request)
    return redirect('blogapp:home')


@login_required
def create_article_view(request):
    if request.method == 'POST':
        form = ArticleForms(request.POST)
        if form.is_valid():
            new_article = form.save(commit=False)
            new_article.author = request.user
            new_article.save()
            return redirect('blogapp:home')
        
    else:
        form = ArticleForms()
        
    return render(
        request, 
        'create_update_article.html', 
        {'form': form, 
        'action': 'Creer'
    })
    
def detail_article_view(request, pk):
    article = get_object_or_404(Article, pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'detail_article.html', context)