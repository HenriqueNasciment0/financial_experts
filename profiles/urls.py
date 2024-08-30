from rest_framework.routers import DefaultRouter
from .views import CompanyProfileViewSet, ExpertProfileViewSet

router = DefaultRouter()
router.register(r"company-profiles", CompanyProfileViewSet)
router.register(r"expert-profiles", ExpertProfileViewSet)

urlpatterns = router.urls
