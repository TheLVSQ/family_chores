from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.contrib.auth import views as auth_views
from .views import FamilyMemberViewSet, ChoreViewSet, home, add_family_member, add_chore

router = DefaultRouter()
router.register(r"familymembers", FamilyMemberViewSet)
router.register(r"chores", ChoreViewSet)


urlpatterns = [
    path("", home, name="home"),
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("api/v1/", include(router.urls)),
    path("add_family_member/", add_family_member, name="add_family_member"),
    path("add_chore/", add_chore, name="add_chore"),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="chores/login.html"),
        name="login",
    ),
]
