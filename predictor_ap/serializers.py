from rest_framework import serializers, views, status
from rest_framework.response import Response
from . import models

class PremierLeagueTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PremierLeagueTeam
        fields = (
            'id',
            'name',
            'location',
            'league',
        )

class PremierLeagueMatchSerializer(serializers.ModelSerializer):
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

class WorldCupMatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.WorldCupMatch
        fields = (
            'id',
            'match_date',
            'group',
            'home_team',
            'away_team',
            'home_score',
            'away_score',
            'result',
        )

class LaLigaTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LaLigaTeam
        fields = (
            'id',
            'name',
            'location',
            'league',
        )

class BundesligaTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BundesligaTeam
        fields = (
            'id',
            'name',
            'location',
            'league',
        )
