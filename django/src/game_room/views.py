from django.shortcuts import render
from rest_framework import viewsets
from game_room.models import GameRoom, Team, QueueRoom
from game_room.serializers import GameRoomSerializer, TeamSerializer, QueueRoomSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from users.models import CustomUser
from rest_framework.views import APIView
from game_room.utils import create_game_room
# Create your views here.

class GameRoomViewSet(viewsets.ModelViewSet):
    serializer_class = GameRoomSerializer
    queryset = GameRoom.objects.all()

class TeamViewSet(viewsets.ModelViewSet):
    serializer_class = TeamSerializer
    queryset = Team.objects.all()

    @action(detail=False, methods=['get'])
    def get_team(self, request):
        queueroom = QueueRoom.objects.get_or_create(id=1)[0]
        if queueroom.players_waiting.all().count() >= 4:
            players = queueroom.players_waiting.all()[:4]
            create_game_room(players[0], players[1], players[2], players[3])
            queueroom.players_waiting.remove(*players)

        user_id = request.query_params.get(
            'user_id'
        )
        user = CustomUser.objects.get(id=user_id)
        queryset = user.teams.all()
        print(user, queryset)
        serialize = TeamSerializer(queryset, many=True)
        return Response(serialize.data)


class QueueUp(APIView):
    def get(self, request, format=None):
        queueroom = QueueRoom.objects.get_or_create(id=1)[0]
        user_id = request.query_params.get('user_id')
        user = CustomUser.objects.get(id=user_id)
        queueroom.players_waiting.add(user)
        queueroom.save()
        serialize = QueueRoomSerializer(queueroom)

        return Response(serialize.data)