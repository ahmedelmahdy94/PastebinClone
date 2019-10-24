from .models import *
from rest_framework import serializers
from django.db.models import Avg
from rest_framework.serializers import (
    EmailField,
    HyperlinkedModelSerializer,
    ModelSerializer,
    ValidationError
    )


class PostSerializer(ModelSerializer):
    class Meta:
        model = Posts
        fields = '__all__'
