from django.shortcuts import render
from rest_framework import viewsets          # add this
from .serializers import NoteSerializer     # add this
from .models import Note                     # add this


class NoteView(viewsets.ModelViewSet):       # add this
    serializer_class = NoteSerializer          # add this
    queryset = Note.objects.all()              # add this
