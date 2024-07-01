# forms.py
# forms.py
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _

class RegistroForm(UserCreationForm):
    email = forms.EmailField(label=_('Correo electrónico'), required=True)
    first_name = forms.CharField(label=_('Nombre'), max_length=30, required=True)
    last_name = forms.CharField(label=_('Apellido'), max_length=30, required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        labels = {
            'username': _('Nombre de usuario'),
            'password1': _('Contraseña'),
            'password2': _('Confirmar contraseña'),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
        return user


