from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.player_form, name = "player_insert"), #get and post request for inserts
    #path("list/", include("nba_app.urls")),
    #the path below is for insert and update operations
    path('<int:id>/', views.player_form, name = "player_update"), #get and post request for update operation
    path("delete/<int:id>/", views.delete_from_list, name = 'list_delete'),
    path('list/', views.player_list, name = "player_list" ), #get display all record
    path('', views.index, name='index'),
    #from Gio's tutorial


    path('randominsert', views.randominsert, name='randominsert'),
    path('randomdelete', views.randomdelete, name='randomdelete'),
    #path('player_insert', views.player_insert, name='player_insert'),
    #path('player_update', views.player_update, name='player_update'),
    #path('player_select', views.player_select, name='player_select'),
    #path('player_delete', views.player_delete, name='player_delete')
    #these paths caused a bug
    path('teams',views.team_list,name='team_list'),
    path('teamsform',views.team_form,name="teamsform")
]
