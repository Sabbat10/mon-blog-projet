from django.urls import path
from blogapp.views import home_view

 
app_name = 'blogapp'

urlpatterns = [
    path('', home_view, name='home'),
]