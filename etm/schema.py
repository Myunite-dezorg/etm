from graphene import Argument, Field, ID, ObjectType, Schema
from graphene_django import DjangoConnectionField
from note.models import Note
from .gql.notes.types import NoteType
from graphene_django.filter import DjangoFilterConnectionField


class Query(ObjectType):
    notes = DjangoConnectionField(NoteType, filterset_class=NoteFilter)
    note = Field(NoteType, id=Argument(ID, required=True))

    def resolve_notes(root, info, **kwargs):
        return Note.objects.all()

    def resolve_note(root, info, **kwargs):
        return Note.objects.get(id=kwargs.get('id'))


schema = Schema(query=Query)
