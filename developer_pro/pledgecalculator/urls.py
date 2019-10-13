from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('calc', views.calc, name='calc'),
    path('stocks', views.stocks, name='stocks'),
]