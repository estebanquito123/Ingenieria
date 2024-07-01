from django.contrib import admin

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario

class UsuarioAdmin(UserAdmin):
    model = Usuario
    list_display = ['username', 'first_name', 'last_name', 'email', 'direccion', 'celular', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('direccion', 'celular')}),
    )

admin.site.register(Usuario, UsuarioAdmin)

