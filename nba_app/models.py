from django.db import models

# Create your models here.
class Player(models.Model):
    player_id = models.IntegerField(default=0, primary_key = True)
    playerName = models.CharField(max_length=150)

    def __str__(self):
        return self.playerName

class Teams(models.Model):
    team = models.IntegerField(default = 0, primary_key = True)
    player = models.ForeignKey(Player, on_delete = models.CASCADE)

class PlayerStats(models.Model):
    player = models.OneToOneField(Player, on_delete = models.CASCADE, primary_key = True)
    score = models.IntegerField(default=0)
    rebound = models.IntegerField(default=0)
    assists = models.IntegerField(default=0)
    blocks = models.IntegerField(default=0)
