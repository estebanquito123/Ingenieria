from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    direccion = models.CharField(max_length=255)
    celular = models.CharField(max_length=15)

