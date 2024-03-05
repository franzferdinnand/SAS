from django.contrib import admin
from django.urls import path
from jobs.views import JobListView, JobProfileView

app_name = "jobs"

urlpatterns = [
    path("", JobListView.as_view(), name="job_list"),
    path("jobprofile/", JobProfileView.as_view(), name="job_profile"),
]
