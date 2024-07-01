from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario
from django.utils.translation import gettext_lazy as _

class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True, label=_('Correo electrónico'))
    direccion = forms.CharField(max_length=255, required=True, label=_('Dirección'))
    celular = forms.CharField(max_length=15, required=True, label=_('Celular'))

    class Meta:
        model = Usuario
        fields = ['username', 'first_name', 'last_name', 'email', 'direccion', 'celular', 'password1', 'password2']
        labels = {
            'username': _('Nombre de usuario'),
            'first_name': _('Nombre'),
            'last_name': _('Apellido'),
            'password1': _('Contraseña'),
            'password2': _('Confirmar contraseña'),
        }
        error_messages = {
            'username': {
                'unique': _("Este nombre de usuario ya está en uso."),
            },
            'email': {
                'unique': _("Este correo electrónico ya está en uso."),
            },
        }




