from django.contrib import admin
from .models import Note, Profile


class NoteInline(admin.StackedInline):
    model = Note
    extra = 1


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "short_content", "creation_date", "update_date")
    readonly_fields = ("creation_date", "update_date")
    list_display_links = ("id", "title")

    search_fields = ("title", "content")
    list_filter = ("creation_date", "update_date")


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "bio", "birth_date")
    list_filter = ("user", "bio", "birth_date")
    list_select_related = ["user"]
    inlines = [NoteInline]
