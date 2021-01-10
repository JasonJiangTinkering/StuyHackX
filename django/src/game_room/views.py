from django.shortcuts import render
from rest_framework import viewsets
from game_room.models import GameRoom
from game_room.serializers import GameRoomSerializer
# Create your views here.

class GameRoomViewSet(viewsets.ModelViewSet):
    serializer_class = GameRoomSerializer
    queryset = GameRoom.objects.all()