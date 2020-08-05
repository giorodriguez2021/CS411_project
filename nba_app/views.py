from django.contrib import messages
from django.conf import settings
from django.db.models import Count
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404, render, redirect
from django.db import connection
from .forms import PlayerForm,TeamForm
import random
from .models import Player,Team
import csv

# Create your views here.
#front end functions below

#populates the teams table
team_dict = {}
with open("nba_app/teams_import.csv", encoding='utf-8-sig') as f:
    reader = csv.reader(f)
    next(reader,None) #skip the headers
    for row in reader:
        _, created = Team.objects.get_or_create(
        team_id = row[0],
        teamname = row[1],
        )
        team_dict[row[1]] = row[0]


with open("nba_app/to_import.csv", encoding='utf-8-sig') as f:
    reader = csv.reader(f)
    next(reader,None) #skip the headers
    for row in reader:
        _, created = Player.objects.get_or_create(
        player_id = row[0],
        playername = row[1],
        team = Team.objects.get(teamname = (row[2])),
        points = row[3],
        assists = row[4],
        rebounds = row[5],
        blocks = row[6],
        steals = row[7],
        games_played = row[8],
        )


def player_list(request):
    players = Player.objects.all()
    search_term = ''
    if 'search' in request.GET:
        search_term = request.GET['search']
        players = players.filter(playername__icontains=search_term)
    paginator = Paginator(players, 100)
    page = request.GET.get('page')
    players = paginator.get_page(page)
    get_dict_copy = request.GET.copy()
    params = get_dict_copy.pop('page', True) and get_dict_copy.urlencode()
    context = {'player_list': players, 'search_term': search_term} #replace with raw query in final form
    return render(request,"nba_app/player_list.html",context)

TEAM_SQL = """SELECT nba_app_Team.team_id,teamname,count(player_id),sum(points),sum(assists),sum(rebounds),sum(blocks),sum(steals)
FROM nba_app_Team LEFT OUTER JOIN nba_app_Player ON nba_app_Team.team_id=nba_app_Player.team_id
GROUP BY nba_app_Team.team_id;"""
"a"
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

def team_delete(request, id ):
    team = Team.objects.get(pk = id)
    team.delete()
    return redirect("/nba_app/teams")

def team_form(request, id=0):
    if request.method == "GET":
        if id == 0: # if id is 0 then it's an insert operation
            form = TeamForm()
        else:
            team = Team.objects.get(pk = id)
            form = TeamForm(instance = team)
        return render(request,"nba_app/team_form.html",{'form':form})
    else:
        if id == 0:
            form = TeamForm(request.POST)
        else:
            team = Team.objects.get(pk = id)
            form = TeamForm(request.POST, instance = team)
        if form.is_valid():
            form.save()
        return redirect("/nba_app/teams")


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

def recommended_list(request):
    cur = connection.cursor()
<<<<<<< HEAD
    cur.execute(open('advancedquery.sql').read())

    context = {'recommended_list',}
    players = cur.fetchall()
    return render(request,"nba_app/recommended_list.html")
=======
    cur.execute(open('advancedquery.sql','r').read())
    fields = ["pts","ast","reb","blk","stl","gp"]
    inserts = tuple([request.GET.get(f,"NULL") for f in fields])
    rsql = "SELECT * FROM (SELECT test(%s,%s,%s,%s,%s,%s,False)) AS R LIMIT 100" % inserts
    cur.execute(rsql)
    r = cur.fetchall()
    print(r)
    res = list(map(lambda x: eval(x[0]),r))
    return render(request,"nba_app/recommended_list.html",{"player_list":res})
>>>>>>> 060a66f4632e932b521936a271ce8e71207b4257
