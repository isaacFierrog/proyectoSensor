from email.mime import base
from posixpath import basename
from rest_framework.routers import DefaultRouter
from .views import ValorViewSet


router = DefaultRouter()

router.register(r"valores", ValorViewSet, basename="valores")

urlpatterns = router.urls
