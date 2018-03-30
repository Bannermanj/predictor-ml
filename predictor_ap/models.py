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
