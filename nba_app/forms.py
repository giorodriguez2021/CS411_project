from django import forms
from .models import Player

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = '__all__'
        labels = {
            "player_id": "Player ID",
            "playername" : "Player Name",
            "team" : "Team",
            "points" : "PTS",
            "assists" : "AST",
            "rebounds" : "REB",
            "blocks" : "BLK",
            "steals" : "STL"

        }
    def __init__(self, *args, **kward):
        super(PlayerForm,self).__init__(*args, **kward)
<<<<<<< HEAD
        self.fields['team'].empty_label = "Select"
=======
        self.fields['playername'].empty_label = "Select"

>>>>>>> 1a38a86de265b93039f178325d0a05390f9a1fe1
