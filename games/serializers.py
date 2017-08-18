# -*- coding: utf-8 -*-

from rest_framework import serializers

from games.models import GameCategory, Game, Player, PlayerScore


class GameCategorySerializer(serializers.HyperlinkedModelSerializer):
    """ Game category class"""
    games = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='game-detail')

    class Meta:
        model = GameCategory
        fields = (
            'url',
            'pk',
            'name',
            'games'
        )


class GameSerializer(serializers.HyperlinkedModelSerializer):
    """Game class"""
    game_category = serializers.SlugRelatedField(queryset=GameCategory.objects.all(), slug_field='name')

    class Meta:
        model = Game
        fields = (
            'url',
            'game_category',
            'name',
            'release_date',
            'played'
        )


class ScoreSerializer(serializers.HyperlinkedModelSerializer):
    """Score"""
    game = GameSerializer()

    class Meta:
        model = PlayerScore
        fields = (
            'url',
            'pk',
            'score',
            'score_date',
            'game'
        )


class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    """Player"""
    score = ScoreSerializer(many=True, read_only=True)
    gender = serializers.ChoiceField(choices=Player.GENDER_CHOICES)
    gender_description = serializers.CharField(source='get_gender_display', read_only=True)

    class Meta:
        model = Player
        fields = (
            'url',
            'name',
            'gender',
            'gender_description',
            'score'
        )


class PlayerScoreSerializer(serializers.HyperlinkedModelSerializer):
    """Player score"""
    player = serializers.SlugRelatedField(queryset=Player.objects.all(), slug_field='name')
    game = serializers.SlugRelatedField(queryset=Game.objects.all(), slug_field='name')

    class Meta:
        model = PlayerScore
        fields = (
            'url',
            'pk',
            'score',
            'score_date',
            'player',
            'game'
        )
