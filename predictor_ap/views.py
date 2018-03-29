# -*- coding: utf-8 -*-
# from __future__ import unicode_literals
from django.shortcuts import render
from rest_framework import generics, viewsets
from . import models
from . import serializers

class TeamViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = models.Team.objects.all()
    serializer_class = serializers.TeamSerializer
