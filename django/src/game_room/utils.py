from twilio.rest import Client
from twilio.jwt.access_token import AccessToken
from twilio.jwt.access_token.grants import VideoGrant
from game_room.models import GameRoom, Team

from decouple import config

from users.models import CustomUser

def create_room(room_name):
    # Your Account Sid and Auth Token from twilio.com/console
    # and set the environment variables. See http://twil.io/secure
    account_sid = config('TWILIO_ACCOUNT_SID')
    auth_token = config('TWILIO_AUTH_TOKEN')
    client = Client(account_sid, auth_token)

    room = client.video.rooms.create(unique_name=room_name)

    return room

def create_access_token(user, room_name):
    account_sid = config('TWILIO_ACCOUNT_SID')
    api_key = config('TWILIO_API_KEY')
    api_secret = config('TWILIO_API_SECRET')

    # required for Video grant
    identity = user.nickname

    # Create Access Token with credentials
    token = AccessToken(account_sid, api_key, api_secret, identity=identity)

    # Create a Video grant and add to token
    video_grant = VideoGrant(room=room_name)
    token.add_grant(video_grant)

    # Return token info as JSON
    return token.to_jwt()

def create_game_room(user1, user2, user3, user4):
    game_room = GameRoom.objects.create()

    # creating team one and its room
    room = create_room(user1.nickname + " - " + user2.nickname)

    team1 = Team.objects.create(room_sid=room.sid)

    # adding team players
    team1.users.add(user1, user2)

    # creating access token per user
    team1.access_token1 = create_access_token(user1, room.unique_name)
    team1.access_token2 = create_access_token(user2, room.unique_name)

    # adding team1 to the game room
    game_room.teams.add(team1)

    # creating team two and its room
    room = create_room(user3.nickname + " - " + user4.nickname)

    team2 = Team.objects.create(room_sid=room.sid)

    # adding team players
    team2.users.add(user3, user4)

    # creating access token per user
    team2.access_token1 = create_access_token(user3, room.unique_name)
    team2.access_token2 = create_access_token(user4, room.unique_name)

    # adding team2 to the game room
    game_room.teams.add(team2)


    # saving all models
    team1.save()
    team2.save()
    game_room.save()

    return game_room

def test():
    queryset = CustomUser.objects.all()
    return create_game_room(queryset[1], queryset[0], queryset[3], queryset[2])