# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class PremierLeagueTeam(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    league = models.CharField(max_length=100)

    def __str__(self):
        """A string of the model"""
        return self.name

class PremierLeagueMatch(models.Model):
    match_date = models.DateField(max_length=12)
    home_team = models.CharField(max_length=100)
    away_team = models.CharField(max_length=100)
    home_score = models.PositiveSmallIntegerField(default=0)
    away_score = models.PositiveSmallIntegerField(default=0)
    result = models.PositiveSmallIntegerField(default=00)

    def __str__(self):
        """A string of the model"""
        return self.name

class WorldCupMatch(models.Model):
    match_date = models.DateTimeField(max_length=12)
    group = models.CharField(max_length=25)
    home_team = models.CharField(max_length=100)
    home_team_flag = models.ImageField(default= None)
    away_team = models.CharField(max_length=100)
    away_team_flag = models.ImageField(default= None)
    home_score = models.PositiveSmallIntegerField(default=0)
    away_score = models.PositiveSmallIntegerField(default=0)
    result = models.PositiveSmallIntegerField(default=00)

    def __str__(self):
        """A string of the model"""
        return self.name

class LaLigaTeam(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    league = models.CharField(max_length=100)

    def __str__(self):
        """A string of the model"""
        return self.name

class BundesligaTeam(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    league = models.CharField(max_length=100)

    def __str__(self):
        """A string of the model"""
        return self.name
