from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from Goals.viewsets import GoalViewSet, MilestoneViewSet, UpdateViewSet
from Users.views import (
    HomeView, UserHomeView, UserLoginView, UserRegistrationView
)
from Users.viewsets import FriendshipViewSet, ProfileViewSet, MessageViewSet
 

# DRF router
# DefaultRouter automatically provides list and detail read-only views
# Create, update and delete actions must be custom made however we can call on
# the existing generic ModelViewSet methods (see class)
router = DefaultRouter()
router.register(r"goals", GoalViewSet, basename="goal")
router.register(r"milestones", MilestoneViewSet, basename="milestone")
router.register(r"updates", UpdateViewSet, basename="update")
router.register(r"friendships", FriendshipViewSet, basename="friendship")
router.register(r"profiles", ProfileViewSet, basename="profile")
router.register(r"messages", MessageViewSet, basename="message")


urlpatterns = [
    # Django admin
    path("admin/", admin.site.urls),

    # Main site
    path("", HomeView.as_view(), name="home"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", UserRegistrationView.as_view(), name="register"),
    path("<username>/", UserHomeView.as_view(), name="user-home"),

    # DRF router
    path("<username>/data/", include(router.urls)),

    # REST framework testing
    path("api-auth", include("rest_framework.urls")),
]
