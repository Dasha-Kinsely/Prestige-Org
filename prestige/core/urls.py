from rest_framework import routers
from core.api import LeadViewSet

router = routers.DefaultRouter()
router.register('api/core', LeadViewSet, 'core')
urlpatterns = router.urls
