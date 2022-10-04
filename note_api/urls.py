from django.urls import path
from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register("profile", views.ProfileViewSet, basename="profile")

profile_router = routers.NestedDefaultRouter(router, "profile", lookup="profile")
profile_router.register("notes", views.NoteViewSet, basename="profile-notes")

urlpatterns = router.urls + profile_router.urls
