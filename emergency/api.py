from drf_spectacular.utils import extend_schema, OpenApiResponse, OpenApiParameter
from rest_framework import generics, permissions

from emergency.models import Emergency
from emergency.serializer import EmergencySerializer


@extend_schema(tags=['Emergency'])
class EmergencyAPIView(generics.ListCreateAPIView):
    serializer_class = EmergencySerializer
    permission_classes = [permissions.AllowAny]
    queryset = Emergency.objects.all().order_by('-id')
