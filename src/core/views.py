from django.shortcuts import render
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "index.html"
    http_method_names = ["get"]


class SupportView(TemplateView):
    template_name = "support.html"  # TODO
    http_method_names = ["get"]
