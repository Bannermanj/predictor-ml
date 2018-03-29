# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from .models import Team


class TeamModelTest(TestCase):

    @classmethod
    def setUp(cls):
        Team.objects.create(name="Team name")
        Team.objects.create(location="a location here")
        Team.objects.create(league="Major League")
