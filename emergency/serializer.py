from rest_framework import serializers

from emergency.models import Emergency


class EmergencySerializer(serializers.ModelSerializer):

    class Meta:
        model = Emergency
        fields = '__all__'
