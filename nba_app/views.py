from django.shortcuts import render
from django.db import connection

f = open("./sql_Test")
sqlcode = f.read()
f.close()
cursor = connection.cursor()
cursor.execute(sqlcode)

# Create your views here.
from django.http import HttpResponse
def index(request):
    cur = connection.cursor()
    cur.execute("SELECT * from Team");
    dat = cur.fetchall()
    return HttpResponse("Hello, world. You're at the CS411 project.<br>"+"team data: "+str(dat))