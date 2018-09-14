from rest_framework import generics

from .models import Audio
from .serializers import AudioSerializer


class AudioListView(generics.ListAPIView):
    serializer_class = AudioSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return Audio.objects.all()
