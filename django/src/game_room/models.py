from django.db import models

# Create your models here.
class GameRoom(models.Model):
    teams = models.ManyToManyField("game_room.Team", verbose_name='Teams', related_name='game_room', blank=True, null=True)

    def __str__(self):
        return "game_room," + str(self.id)

class Team(models.Model):
    
    users = models.ManyToManyField("users.CustomUser", verbose_name="Team Players", related_name='team_members')
    room_sid = models.CharField("Room Sid", max_length=100, blank=True, null=True)
    access_token1 = models.CharField("accesstoken", max_length=100, blank=True, null=True)
    access_token2 = models.CharField("accestoken", max_length=100, blank=True, null=True)
    score = models.IntegerField('Team Score', blank=True, null=True)

    def __str__(self):
        return "team," + str(self.id)
