from rest_framework import serializers
from .models import Profile, Note


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ("id", "title", "content", "creation_date", "update_date")


class NoteCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ("id", "title", "content", "creation_date", "update_date")

    def create(self, validated_data):
        user_pk = self.context["user_pk"]
        profile, created = Profile.objects.get_or_create(user_id=user_pk)
        instance = Note.objects.create(profile=profile, **validated_data)
        return instance


class ProfileSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    notes = NoteSerializer(many=True, read_only=True)

    class Meta:
        model = Profile
        fields = ("id", "user", "bio", "birth_date", "notes")


class ProfileCreateSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)

    class Meta:
        model = Profile
        fields = ("id", "bio", "birth_date")

    def create(self, validated_data):
        user = self.context["user"]
        instance = Profile.objects.create(user=user, **validated_data)
        return instance
