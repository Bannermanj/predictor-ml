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
