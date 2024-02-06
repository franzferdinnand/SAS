from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

from core.mangers import CustomUserManager


class UserAccount(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(_('First Name'), max_length=255)
    last_name = models.CharField(_('Last Name'), max_length=255)
    birth_date = models.DateField(null=True)
    phone_number = PhoneNumberField(_('Phone Number'), max_length=16, blank=False, unique=True)
    passport_number = models.CharField(_('Passport'), max_length=20, blank=False, unique=True)
    pesel = models.IntegerField(_('PESEL'), max_length=11, unique=True, blank=True, null=True)
    email = models.EmailField(_('Email'), max_length=160, unique=True)
    photo = models.ImageField(_('Photo'), default='', upload_to='media/photos')

    is_staff = models.BooleanField(
        _('is staff'),
        default=False
    )

    is_active = models.BooleanField(
        _('is active'),
        default=True
    )
    USERNAME_FIELD = "passport_number"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    objects = CustomUserManager()

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

