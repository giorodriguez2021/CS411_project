from django.contrib import messages
from django.conf import settings
from django.db.models import Count
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404, render, redirect
from django.db import connection
from .forms import PlayerForm
import random
<<<<<<< HEAD
from .models import Player
from .models import Team
=======
from .models import Player,Team
>>>>>>> 1a38a86de265b93039f178325d0a05390f9a1fe1
# Create your views here.
#front end functions below
def player_list(request):
    players = Player.objects.all()
    search_term = ''
    if 'search' in request.GET:
        search_term = request.GET['search']
        players = players.filter(playername__icontains=search_term)
    paginator = Paginator(players, 10)
    page = request.GET.get('page')
    players = paginator.get_page(page)
    get_dict_copy = request.GET.copy()
    params = get_dict_copy.pop('page', True) and get_dict_copy.urlencode()
    context = {'player_list': players, 'search_term': search_term} #replace with raw query in final form
    return render(request,"nba_app/player_list.html",context)

TEAM_SQL = """SELECT team_id,teamname,sum(points),sum(assists),sum(rebounds),sum(blocks),sum(steals)
FROM nba_app_Team NATURAL JOIN nba_app_Player
GROUP BY team_id;"""

def team_list(request):
    tsql = TEAM_SQL
    cur = connection.cursor()
    cur.execute(TEAM_SQL)
    teams = cur.fetchall()
    search_term = ''
    if 'search' in request.GET:
        search_term = request.GET['search']
        teams = list(filter(lambda t: search_term in t[1],teams))
    context = {'team_list':teams,'search_term':search_term}
    return render(request,"nba_app/team_list.html",context)

def delete_team(request, id ):
    team = Team.objects.get(pk = id)
    team.delete()
    return redirect("/nba_app/teams")
def team_form(request, id=0):
    if request.method == "GET":
        if id == 0: # if id is 0 then it's an insert operation
            form = PlayerForm()
        else:
            player = Player.objects.get(pk = id)
            form = PlayerForm(instance = player)
        return render(request,"nba_app/player_form.html",{'form':form})
    else:
        if id == 0:
            form = PlayerForm(request.POST)
        else:
            player = Player.objects.get(pk = id)
            form = PlayerForm(request.POST, instance = player)
        if form.is_valid():
            form.save()
        return redirect("/nba_app/list")


def player_form(request, id=0):
    if request.method == "GET":
        if id == 0: # if id is 0 then it's an insert operation
            form = PlayerForm()
        else:
            player = Player.objects.get(pk = id)
            form = PlayerForm(instance = player)
        return render(request,"nba_app/player_form.html",{'form':form})
    else:
        if id == 0:
            form = PlayerForm(request.POST)
        else:
            player = Player.objects.get(pk = id)
            form = PlayerForm(request.POST, instance = player)
        if form.is_valid():
            form.save()
        return redirect("/nba_app/list")

def delete_from_list(request, id ):
    player = Player.objects.get(pk = id)
    player.delete()
    return redirect("/nba_app/list")
from django.http import HttpResponse
def index(request):
    return HttpResponse("Hello, world. You're at the CS411 project.")
def list_overview(request):
    players = Player.objects.all()
    return render(request, 'overviews/overview.html', {'players' : players, 'search_term': search_term })
#back end stuff below
def randominsert(request):
    newplayer = "RandomPlayer"+str(random.randint(1,999))
    cur = connection.cursor()
    cur.execute("SELECT max(player_id) FROM nba_app_Player;")
    newid = cur.fetchone()[0]+1
    cur.execute("INSERT INTO nba_app_Player VALUES (%d,'%s');" % (newid,newplayer))
    return HttpResponse("Added player %s with id %d" % (newplayer,newid))
def randomdelete(request):
    cur = connection.cursor()
    cur.execute("SELECT * FROM nba_app_Player WHERE playername LIKE 'RandomPlayer%';")
    rands = ', '.join([a[1] for a in cur.fetchall()])
    if not rands:
        rands = "(none)"
    cur.execute("DELETE FROM nba_app_Player WHERE playerName LIKE 'RandomPlayer%';")
    return HttpResponse("Deleted random players: %s" % rands)
"""
/player_insert?id=ID&name=NAME
"""
def player_insert(request):
    print("PLAYER INSERT")
    pid = request.GET.get('id')
    pname = request.GET.get('name')
    if pid==None or pname==None:
        return HttpResponse("Bad request")
    pid = int(pid)
    cur = connection.cursor()
    cur.execute("SELECT * FROM nba_app_Player WHERE player_id=%d" % pid)
    if len(cur.fetchall()):
        return HttpResponse("key already exists...")
    cur.execute("INSERT INTO nba_app_Player VALUES (%d,'%s')" % (pid,pname))
    return HttpResponse("Inserted!")
def player_update(request):
    print("PLAYER UPDATE")
    oldid = int(request.GET.get('oldid'))
    if oldid==None:
        return HttpResponse("Bad request")
    cur = connection.cursor()
    cur.execute("SELECT * FROM nba_app_Player WHERE player_id=%d" % oldid)
    t = cur.fetchone()
    if not t:
        return HttpResponse("Player not found...")
    _,oldname = t
    pid = int(request.GET.get('id',oldid))
    pname = request.GET.get('name',oldname)
    cur.execute("UPDATE nba_app_Player SET player_id=%d,playername='%s' where player_id=%d" % (pid,pname,oldid))
    return HttpResponse("Updated!")
def player_select(request):
    print("PLAYER SELECT")
    cur = connection.cursor()
    cur.execute("SELECT * FROM nba_app_Player")
    return HttpResponse(str(cur.fetchall()))
def player_delete(request):
    print("PLAYER DELETE")
    print("DELETE")
    pid = request.GET.get('id')
    if pid==None:
        return HttpResponse("Bad request")
    pid = int(pid)
    cur = connection.cursor()
    cur.execute("SELECT * FROM nba_app_Player WHERE player_id=%d" % pid)
    if not len(cur.fetchall()):
        return HttpResponse("Player not found...")
    cur.execute("DELETE FROM nba_app_Player WHERE player_id=%d" % pid)
    return HttpResponse("Deleted!")
