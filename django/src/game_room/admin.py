from django.contrib import admin
from game_room.models import GameRoom, Team, QueueRoom
# Register your models here.

admin.site.register(GameRoom)
admin.site.register(Team)
admin.site.register(QueueRoom)
