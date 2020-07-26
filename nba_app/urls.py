from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('randominsert', views.randominsert, name='randominsert'),
    path('randomdelete', views.randomdelete, name='randomdelete')
]
