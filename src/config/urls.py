from django.contrib import admin
from django.urls import path, include

from core.views import IndexView, SupportView
from jobs.views import JobListView, JobProfileView
from user.views import UserProfileView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("core.urls")),
    path("jobs/", JobListView.as_view()),
    path("jobprofile/", JobProfileView.as_view(), name='job_rofile'),
    path("userprofile/", UserProfileView.as_view(), name='user_profile'),

]
