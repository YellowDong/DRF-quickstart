from django.conf.urls import url, include
from rest_framework import routers
from .views import MusicViewSet

router = routers.DefaultRouter()
router.register(r'myapp', MusicViewSet)


urlpatterns = [
    url(r'', include(router.urls))
]