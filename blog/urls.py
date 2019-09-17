from rest_framework import routers
from .api import LeadViewSet

router = routers.DefaultRouter()
router.register('api/blogs',LeadViewSet,'blog')

urlpatterns = router.urls