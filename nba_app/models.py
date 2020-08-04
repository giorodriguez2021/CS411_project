from django.db import models
from django.db import connection

# Create your models here.

class Team(models.Model):
    team_id = models.IntegerField(default = 0, primary_key = True) # possibly delete this
    teamname = models.CharField(max_length=150)
    def __str__(self):
        return self.teamname

class Player(models.Model):
    player_id = models.IntegerField(default=0, primary_key = True)
    playername = models.CharField(max_length=150)
    team = models.ForeignKey(Team,on_delete = models.CASCADE)
    points = models.IntegerField(default=0)
    assists = models.IntegerField(default=0)
    rebounds = models.IntegerField(default=0)
    blocks = models.IntegerField(default=0)
    steals = models.IntegerField(default=0)
#needed for drop down menu
    def __str__(self):
        return self.playername

class Game(models.Model):
    team1 = models.ForeignKey(Team,on_delete = models.CASCADE, related_name = "team1")
    team2 = models.ForeignKey(Team,on_delete = models.CASCADE, related_name = "team2")
    score1 = models.IntegerField(default=0)
    score2 = models.IntegerField(default=0)
