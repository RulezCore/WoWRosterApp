from .models import Raid
from .serializers import RaidSerializer
from rest_framework import viewsets

# Create your views here.


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Raid.objects.all()
    serializer_class = RaidSerializer
