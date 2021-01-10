from django.shortcuts import render
from rest_framework import viewsets
from .models import Song
from .serializers import SongSerializer


class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all().order_by('name')
    serializer_class = SongSerializer
