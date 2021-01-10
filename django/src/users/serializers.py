from rest_framework import serializers
from users.models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            'id',
            'email',
            'first_name',
            'last_name',
            'nickname',
            'school',
            'grade',
            'default_topics',
            'interest',
            'score',
            'friends'
        ]