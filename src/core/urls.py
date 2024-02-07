from django.contrib import admin
from django.urls import include, path

from core.views import IndexView, SupportView
from jobs.views import JobListView, JobProfileView
from user.views import UserProfileView

app_name = "core"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("support/", SupportView.as_view(), name="support"),
]
