from django.urls import path
from blogapp.views import home_view, connexion_view, inscription_view, deconnexion_view, create_article_view, detail_article_view, update_article_view

 
app_name = 'blogapp'

urlpatterns = [
    path('', home_view, name='home'),
    path('connexion/', connexion_view, name='connexion'),
    path('inscription/', inscription_view, name='inscription'),
    path('deconnexion/', deconnexion_view, name='deconnexion'),
    
    path('article/create/', create_article_view, name='create_article'),
    path('article/<int:pk>/', detail_article_view, name='detail_article'),
    path('article/<int:pk>/update/', update_article_view, name='update_article'),
] 