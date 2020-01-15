from core.models import Lead
from core.serializers import LeadSerializer

from rest_framework import viewsets, permissions


class LeadViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all()  # get from input models
    permission_classes = [
        permissions.AllowAny  # set permission to any types
    ]
    serializer_class = LeadSerializer  # serialize
