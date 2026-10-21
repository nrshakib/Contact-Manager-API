from rest_framework import viewsets

from notes.models import Notes
from notes.serializers import NotesSerializer

class NotesViewSet(viewsets.ModelViewSet):
    queryset = Notes.objects.all()
    serializer_class = NotesSerializer