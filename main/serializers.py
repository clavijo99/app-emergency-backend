from rest_framework import serializers
from main.models import Configuration


class ConfigurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Configuration
        fields = ['key', 'value']


class DefaultResponseSerializer(serializers.Serializer):  # noqa
    detail = serializers.CharField()
