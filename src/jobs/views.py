from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import DetailView, ListView

from jobs.models import JobModel


class JobListView(ListView):
    template_name = "jobs/jobs.html"
    model = JobModel
    context_object_name = "job"


class JobProfileView(DetailView):
    model = JobModel
    template_name = "JobProfile.html"  # TODO
    queryset = JobModel.objects.all()
