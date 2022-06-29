from django.contrib import admin
from django.urls import path, include
from apps.home.views import home


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', home, name='home'),
    path('sensores/', include(('apps.sensor.urls', 'sensor'))),
    path('modulos/', include(('apps.modulo.urls', 'modulo')))
]
