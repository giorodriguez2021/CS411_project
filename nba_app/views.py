from django.shortcuts import render
from django.db import connection
import random

# Create your views here.
from django.http import HttpResponse
def index(request):
    return HttpResponse("Hello, world. You're at the CS411 project.")

def randominsert(request):
    newplayer = "RandomPlayer"+str(random.randint(1,999))
    cur = connection.cursor()
    cur.execute("SELECT max(player_id) FROM nba_app_Player;")
    newid = cur.fetchone()[0]+1
    cur.execute("INSERT INTO nba_app_Player VALUES (%d,'%s');" % (newid,newplayer))
    return HttpResponse("Added player %s with id %d" % (newplayer,newid))

def randomdelete(request):
    print(request.__dict__["path_info"])
    cur = connection.cursor()
    cur.execute("SELECT * FROM nba_app_Player WHERE playername LIKE 'RandomPlayer%';")
    rands = ', '.join([a[1] for a in cur.fetchall()])
    if not rands:
        rands = "(none)"
    cur.execute("DELETE FROM nba_app_Player WHERE playerName LIKE 'RandomPlayer%';")
    return HttpResponse("Deleted random players: %s" % rands)