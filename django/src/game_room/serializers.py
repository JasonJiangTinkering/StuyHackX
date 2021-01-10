from rest_framework import serializers
from game_room.models import GameRoom, Team, QueueRoom

class GameRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameRoom
        fields = '__all__'

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'

class QueueRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = QueueRoom
        fields = '__all__'