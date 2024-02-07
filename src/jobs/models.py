from django.db import models
from django.utils.translation import gettext_lazy as _


class JobModel(models.Model):
    position = models.CharField(_("Position"), max_length=150, null=False)
    city = models.CharField(_("City"), max_length=25, null=False)
    payment = models.FloatField(_("Payment per hour"), max_length=15)
    job_description = models.CharField(_("Job description"), max_length=700)
