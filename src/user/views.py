from django.contrib.auth import get_user_model, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from django.views.generic import DetailView, RedirectView, CreateView

from core.TokenGenerator import TokenGenerator
from core.form import UserRegistrationForm
from core.services.email_sender import send_registration_email
from user.models import UserAccount


class UserRegistrationView(CreateView):
    template_name = "registration/registration.html"
    form_class = UserRegistrationForm
    success_url = reverse_lazy("core:index")

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.is_active = False
        self.object.save()

        send_registration_email(request=self.request, user_instance=self.object)

        return super().form_valid(form)


class UserLoginView(LoginView):
    ...


class UserLogoutView(LogoutView):
    template_name = 'index.html'


class ActivateUser(RedirectView):
    url = reverse_lazy("core:index")

    def get(self, request, uuid64, token, *args, **kwargs):
        try:
            pk = force_str(urlsafe_base64_decode(uuid64))
            current_user = get_user_model().objects.get(pk=pk)
        except (ValueError, get_user_model().Does_not_exist, TypeError):
            return HttpResponse("Wrong data!")

        if current_user and TokenGenerator().check_token(current_user, token):
            current_user.is_active = True
            current_user.save()
            login(request, current_user)

            return super().get(request, *args, **kwargs)
        return HttpResponse("Wrong data!")


class UserProfileView(LoginRequiredMixin, DetailView):
    model = UserAccount
    template_name = "UserProfile.html"  # TODO
    queryset = UserAccount.objects.all()
