from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('rout', views.rout),
    path('false', views.false),


    	   
]