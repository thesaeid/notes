from uuid import uuid4
from django.db import models
from django.conf import settings
from django.template.defaultfilters import truncatechars


class Profile(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    birth_date = models.DateField(null=True, blank=True)
    # notes = models.ForeignKey(Note, on_delete=models.CASCADE, related_name="profile")

    def __str__(self):
        return self.user.username


class Note(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="notes")

    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def short_content(self):
        return truncatechars(self.content, 20)

    def __str__(self):
        return self.title
