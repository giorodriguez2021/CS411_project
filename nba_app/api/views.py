from rest_framework.generics import ListAPIView, RetrieveAPIView

from nba_app.models import Player
from .serializers import PlayerSerializer

class PlayerListView(ListAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

class PlayerDetailView(RetrieveAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
