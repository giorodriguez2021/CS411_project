from django.db import models

# Create your models here.
class Player(models.Model):
    player_id = models.IntegerField(default=0, primary_key = True)
    playerName = models.CharField(max_length=150)

class Teams(models.Model):
    player = models.ForeignKey(Player, on_delete = models.CASCADE)
