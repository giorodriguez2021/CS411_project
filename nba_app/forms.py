from django import forms
from .models import Player

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = '__all__'
        labels = {
            "player_number": "Player ID",
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
        self.fields['team'].empty_label = "Select"
