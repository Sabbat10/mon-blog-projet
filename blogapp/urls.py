from django.urls import path
from blogapp.views import home_view, connexion_view, inscription_view, deconnexion_view

 
app_name = 'blogapp'

urlpatterns = [
    path('', home_view, name='home'),
    path('connexion/', connexion_view, name='connexion'),
    path('inscription/', inscription_view, name='inscription'),
    path('deconnexion/', deconnexion_view, name='deconnexion'),
]