from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index/servicios', views.servicios, name='servicios'),
    path('index/nosotros', views.nosotros, name='nosotros'),
    path('index/login', views.login, name='login'),
    path('servicios/imperdibles', views.login, name='imperdibles'),
    path('servicios/aprendizaje', views.login, name='aprendizaje'),
]