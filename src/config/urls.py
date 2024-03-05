from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path

from config.settings import dev
from core.views import IndexView, SupportView
from jobs.views import JobListView, JobProfileView
from user.views import UserProfileView, UserLoginView, UserLogoutView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("core.urls")),
    path("jobs/", include("jobs.urls")),
    path("userprofile/", UserProfileView.as_view(), name="user_profile"),
]
