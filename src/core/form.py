from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ["first_name", "last_name", "phone_number", "passport_number", "email", "password1", "password2"]

        def clean(self):
            _cleaned_data = super().clean()

            if not bool(_cleaned_data["passport_number"]):
                if get_user_model().objects.filter(passport_number=_cleaned_data["passport_number"]).exists():
                    raise ValidationError("User with this phone number already exists!!!")

            return _cleaned_data