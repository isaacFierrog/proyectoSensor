from django.contrib import admin
from django.urls import path, include
from apps.home.views import home


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', home, name='home'),
    path('sensor/', include(('apps.sensor.urls', 'sensor'))),
    path('modulo/', include(('apps.modulo.urls', 'modulo')))
]
