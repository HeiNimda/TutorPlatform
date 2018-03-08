# coding=utf-8

from django.contrib.auth.models import User, Group
from rest_framework import serializers
from . import models
from common import serializers as common_serializer


class FavoriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.UserFavorite
        fields = "__all__"



