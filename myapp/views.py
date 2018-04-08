from .models import Music
from rest_framework import viewsets
from .serializers import MusicSerializer


class MusicViewSet(viewsets.ModelViewSet):
    queryset = Music.objects.all().order_by('-created')
    serializer_class = MusicSerializer
