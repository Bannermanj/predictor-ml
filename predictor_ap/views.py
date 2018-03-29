# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from rest_framework import generics
from . import models
from . import serializers

# Create your views here.

class ListTeam(generics.ListCreateAPIView):
    queryset = models.Team.objects.all()
    serializer_class = serializers.TeamSerializer

class DetailTeam(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Team.objects.all()
    serializer_class = serializers.TeamSerializer
