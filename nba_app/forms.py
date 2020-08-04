from django import forms
from .models import Player,Team

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = '__all__'
        labels = {
            "player_number": "Player ID",
            "playername" : "Player Name"
        }
    def __init__(self, *args, **kward):
        super(PlayerForm,self).__init__(*args, **kward)
        self.fields['playername'].empty_label = "Select"

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = '__all__'
        labels = {
            "team_id": "Team ID",
            "teamname":"Team Name"
        }
    def __init__(self, *args, **kward):
        super(TeamForm,self).__init__(*args,**kward)
        self.fields['teamname'].empty_label = "Select"