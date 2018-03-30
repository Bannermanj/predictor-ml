# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from rest_framework import generics, viewsets
from . import models
from . import serializers

class PremierLeagueTeamViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = models.PremierLeagueTeam.objects.all()
    serializer_class = serializers.PremierLeagueTeamSerializer

class LaLigaTeamViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = models.LaLigaTeam.objects.all()
    serializer_class = serializers.LaLigaTeamSerializer

class BundesligaTeamViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = models.BundesligaTeam.objects.all()
    serializer_class = serializers.BundesligaTeamSerializer
