from django.urls import path
from . import views


urlpatterns = [
    path('', views.szavak, name = 'szavak'),
    path('', views.tema, name = 'tema')
]
