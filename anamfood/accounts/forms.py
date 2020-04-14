from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model=get_user_model()
        fields=['last_name','first_name','username','email']