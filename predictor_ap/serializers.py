from rest_framework import serializers, views, status
from rest_framework.response import Response
from . import models

class PremierLeagueTeamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.PremierLeagueTeam
        fields = (
            'id',
            'name',
            'location',
            'league',
        )

class PremierLeagueMatchSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.PremierLeagueMatch
        fields = (
            'id',
            'match_date',
            'home_team',
            'away_team',
            'home_score',
            'away_score',
            'result',
        )

class WorldCupMatchSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.WorldCupMatch
        fields = (
            'id',
            'match_date',
            'match_time',
            'group',
            'home_team',
            'away_team',
            'home_score',
            'away_score',
            'result',
        )

class WorldCupMatch2Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.WorldCupMatch
        fields = (
            'id',
            'match_date',
            'match_time',
            'group',
            'home_team',
            'away_team',
            'home_score',
            'away_score',
            'result',
        )

class LaLigaTeamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.LaLigaTeam
        fields = (
            'id',
            'name',
            'location',
            'league',
        )

class BundesligaTeamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.BundesligaTeam
        fields = (
            'id',
            'name',
            'location',
            'league',
        )
