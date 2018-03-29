from rest_framework import serializers
from . import models


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Team
        fields = (
            'id',
            'name',
            'location',
            'league',
        )
