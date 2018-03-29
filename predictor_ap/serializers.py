from rest_framework import serializers
from . import models


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'name',
            'location',
            'league',
        )
        model = models.Team
