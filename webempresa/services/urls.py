from django.urls import path
from . import views


urlpatterns = [
    #path del services , y se dejo en la raiz 
    path('', views.services, name='services'),
 
]