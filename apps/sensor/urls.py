from django.urls import path
from .views import sensores


urlpatterns = [
    path('', sensores, name='sensores')
]