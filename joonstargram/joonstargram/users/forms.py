from django.contrib.auth import forms as admin_forms
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _


from django import forms

User = get_user_model()


class UserChangeForm(admin_forms.UserChangeForm):
    class Meta(admin_forms.UserChangeForm.Meta):
        model = User


class UserCreationForm(admin_forms.UserCreationForm):
    class Meta(admin_forms.UserCreationForm.Meta):
        model = User

        error_messages = {
            "username": {"unique": _("This username has already been taken.")}
        }

class SignUpForm(forms.ModelForm):
    class Meta():
        model = User
        fields = ['email', 'name', 'username', 'password']

        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'メールアドレス'}),
            'name': forms.TextInput(attrs={'placeholder': '氏名'}),
            'username': forms.TextInput(attrs={'placeholder': '使用者名'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'パスワード'}),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        user.is_active = False
        if commit:
            user.save()
        return user
