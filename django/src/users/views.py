from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from rest_auth.registration.views import SocialLoginView
from rest_auth.registration.serializers import SocialLoginSerializer
from rest_framework import viewsets
from users.models import CustomUser
from users.serializers import CustomUserSerializer
from rest_framework.response import Response
from rest_framework.decorators import action



class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    client_class = OAuth2Client
    callback_url = 'localhost:8000'
    serializer_class = SocialLoginSerializer

    def get_serializer(self, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        kwargs['context'] = self.get_serializer_context()
        return serializer_class(*args, **kwargs)


class CustomUserViewSet(viewsets.ModelViewSet):
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()

    @action(detail=True, methods=['get'])
    def add_friend(self, request, pk=None):
        user = self.get_object()
        friend_id = request.query_params.get(
            'friend_id'
        )
        friend_obj = CustomUser.objects.get(id=friend_id)
        
        user.friends.add(friend_obj)

        return Response({'status': 'Friend Added'})

    @action(detail=True, methods=['get'])
    def remove_friend(self, request, pk=None):
        user = self.get_object()
        friend_id = request.query_params.get(
            'friend_id'
        )
        friend_obj = CustomUser.objects.get(id=friend_id)
        
        user.friends.remove(friend_obj)

        return Response({'status': 'Friend Removed'})

    @action(detail=True, methods=['get'])
    def get_friend_list(self, request, pk=None):
        user = self.get_object()
        friends = user.friends.all()
        serializer = CustomUserSerializer(friends, many=True)
        return Response(serializer.data)


    def list(self, request):
        queryset = CustomUser.objects.all().order_by('-score')
        serializer = CustomUserSerializer(queryset, many=True)
        return Response(serializer.data)
