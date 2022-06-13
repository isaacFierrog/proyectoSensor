from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("apps.valor.routes")),
    path("api/", include("apps.sensor.routes")),
]
