# historias_sobre_Deus/urls.py
from django.urls import path
from . import views

urlpatterns = [
path('', views.home, name='historias_sobre_Deus'),
]