from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('randominsert', views.randominsert, name='randominsert'),
    path('randomdelete', views.randomdelete, name='randomdelete'),
    path('player_insert', views.player_insert, name='player_insert'),
    path('player_update', views.player_update, name='player_update'),
    path('player_select', views.player_select, name='player_select'),
    path('player_delete', views.player_delete, name='player_delete')
]
