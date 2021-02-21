from django.shortcuts import render
from rest_framework import viewsets
from game_room.models import GameRoom, Team, QueueRoom
from game_room.serializers import GameRoomSerializer, TeamSerializer, QueueRoomSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from users.models import CustomUser
from rest_framework.views import APIView
from game_room.utils import create_game_room
from django.http import JsonResponse
from django.db.models import Q

from game_room.utils import create_access_token
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

        user_id = request.user.id
        user = CustomUser.objects.get(id=user_id)
        queryset = user.teams.all()
        opponents = user.teams.all()
        if(user.teams.all().exists()):
            opponents = user.teams.all()[0].game_room.all()[
                0].teams.filter(~Q(id=queryset[0].id))

        opponents_serialize = TeamSerializer(opponents, many=True)

        serialize = TeamSerializer(queryset, many=True)
        # print(serialize, opponents_serialize)
        queryroom_serialize = QueueRoomSerializer(queueroom)
        return Response({
            'team': serialize.data,
            'opponents': opponents_serialize.data,
            'queryroom': queryroom_serialize.data
        })

    @action(detail=False, methods=['get'])
    def get_access_token(self, request):
        token = create_access_token(CustomUser.objects.get(id=1), 'cool-room')
        result = {"accessToken": token}
        return Response(result)


class QueueUp(APIView):
    def get(self, request, format=None):
        queueroom = QueueRoom.objects.get_or_create(id=1)[0]
        user_id = request.user.id
        user = CustomUser.objects.get(id=user_id)
        queueroom.players_waiting.add(user)
        queueroom.save()
        serialize = QueueRoomSerializer(queueroom)

        return Response(serialize.data)
