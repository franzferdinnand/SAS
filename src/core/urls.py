from django.contrib import admin
from django.urls import include, path

from core.views import IndexView, SupportView
from jobs.views import JobListView, JobProfileView
from user.views import UserProfileView, UserLogoutView, UserLoginView, UserRegistrationView

app_name = "core"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("registration/", UserRegistrationView.as_view(), name="registration"),
    path("support/", SupportView.as_view(), name="support"),
    path("logout/", UserLogoutView.as_view(), name='logout'),
    path("login/", UserLoginView.as_view(), name='login'),
]
