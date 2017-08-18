# coding=utf-8
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse

from games.models import *
from games.serializers import *


class GameCategoryList(generics.ListCreateAPIView):
    """Game category list"""
    queryset = GameCategory.objects.all()
    serializer_class = GameCategorySerializer
    name = 'gamecategory-list'


class GameCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    """Game category detail"""
    queryset = GameCategory.objects.all()
    serializer_class = GameCategorySerializer
    name = 'gamecategory-detail'


class GameList(generics.ListCreateAPIView):
    """Game list"""
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    name = 'game-list'


class GameDetail(generics.RetrieveUpdateDestroyAPIView):
    """Game detail"""
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    name = 'game-detail'


class PlayerList(generics.ListCreateAPIView):
    """Player list"""
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    name = 'player-list'


class PlayerDetail(generics.RetrieveUpdateDestroyAPIView):
    """Player detail"""
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    name = 'player-detail'


class PlayerScoreList(generics.ListCreateAPIView):
    """Player score list"""
    queryset = PlayerScore.objects.all()
    serializer_class = PlayerScoreSerializer
    name = 'playerscore-list'


class PlayerScoreDetail(generics.RetrieveUpdateDestroyAPIView):
    """Player score detail"""
    queryset = PlayerScore.objects.all()
    serializer_class = PlayerScoreSerializer
    name = 'playerscore-detail'


class ApiRoot(generics.GenericAPIView):
    """Api root"""
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        """Method to response of list items"""
        return Response({
            'players': reverse(PlayerList.name, request=request),
            'game-categories': reverse(GameCategoryList.name, request=request),
            'games': reverse(GameList.name, request=request),
            'scores': reverse(PlayerScoreList.name, request=request)
        })
