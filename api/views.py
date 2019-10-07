from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, views
from django.shortcuts import get_object_or_404
from .models import Raid, RaidAssistance
from .serializers import RaidSerializer
from rest_framework import viewsets

# Create your views here.


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Raid.objects.all()
    serializer_class = RaidSerializer


class MarcarAsistenciaRaid(views.APIView):
    def post(self, request):
        if request.user.is_authenticated:
            raid_assistance = get_object_or_404(
                RaidAssistance, id=self.request.data.get('id', 0))
            raid_assistance.assistance = not raid_assistance.assistance
            raid_assistance.save()
            content = {'id': raid_assistance.id,
                       'assistance': raid_assistance.assistance}
            return Response(content)
