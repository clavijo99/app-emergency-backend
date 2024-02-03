from django.urls import path
from .api import EmergencyAPIView


api_urls = ([
    path('emergency', EmergencyAPIView.as_view(), name='emergency')

] , 'Emergency')

urlpatterns = [
]
