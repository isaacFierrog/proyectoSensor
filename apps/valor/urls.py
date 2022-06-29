from django.urls import path
from .views import valores


urlpatterns = [
    path('/valores', valores, name='valores')
]
