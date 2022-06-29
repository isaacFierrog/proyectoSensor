from django.urls import path
from .views import modulos


urlpatterns = [
    path('', modulos, name='modulos')
]
