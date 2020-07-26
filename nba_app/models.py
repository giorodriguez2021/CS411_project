from django.db import models
from django.db import connection

"""f = open("./sql_Test")
sqlcode = f.read()
f.close()
cursor = connection.cursor()
cursor.execute(sqlcode)"""

# Create your models here.
class Player(models.Model):
    player_id = models.IntegerField(default=0, primary_key = True)
    playername = models.CharField(max_length=150)

    def __str__(self):
        return self.playername

class Team(models.Model):
    teamID = models.IntegerField(default = 0, primary_key = True)
    teamName = models.CharField(max_length=150)

class OnTeam(models.Model):
    teamID = models.ForeignKey(Team,on_delete = models.CASCADE)
    playerID = models.ForeignKey(Player,on_delete=models.CASCADE)

class PlayerStats(models.Model):
    player = models.OneToOneField(Player, on_delete = models.CASCADE, primary_key = True)
    score = models.IntegerField(default=0)
    rebound = models.IntegerField(default=0)
    assists = models.IntegerField(default=0)
    blocks = models.IntegerField(default=0)

class Game(models.Model):
    team1 = models.ForeignKey(Team,on_delete = models.CASCADE, related_name = "team1")
    team2 = models.ForeignKey(Team,on_delete = models.CASCADE, related_name = "team2")
    score1 = models.IntegerField(default=0)
    score2 = models.IntegerField(default=0)