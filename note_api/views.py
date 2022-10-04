from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Note, Profile
from .serializers import (
    NoteSerializer,
    NoteCreateSerializer,
    ProfileCreateSerializer,
    ProfileSerializer,
)


class NoteViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Note.objects.filter(profile__user=self.request.user)

    def get_serializer_class(self):
        if self.request.method == "POST":
            return NoteCreateSerializer
        return NoteSerializer

    def get_serializer_context(self):
        return {"user_pk": self.request.user.id}


class ProfileViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Profile.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.request.method == "POST":
            return ProfileCreateSerializer
        return ProfileSerializer

    def get_serializer_context(self):
        return {"user": self.request.user}
