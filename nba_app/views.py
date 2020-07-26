from django.shortcuts import render, redirect
from django.db import connection
from .forms import PlayerForm
import random
from .models import Player

# Create your views here.


#front end functions below
def player_list(request):
    context = {'player_list': Player.objects.all()} #replace with raw query in final form
    return render(request,"nba_app/player_list.html",context)

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

from django.http import HttpResponse
def index(request):
    return HttpResponse("Hello, world. You're at the CS411 project.")



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
