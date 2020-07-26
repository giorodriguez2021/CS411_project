from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.player_form),
    #path("list/", include("nba_app.urls")),
    path('list/', views.player_list),
    path('', views.index, name='index'),
    #from Gio's tutorial

    path('randominsert', views.randominsert, name='randominsert'),
    path('randomdelete', views.randomdelete, name='randomdelete'),
    path('player_insert', views.player_insert, name='player_insert'),
    path('player_update', views.player_update, name='player_update'),
    path('player_select', views.player_select, name='player_select'),
    path('player_delete', views.player_delete, name='player_delete')

]
