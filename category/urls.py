from rest_framework.routers import DefaultRouter

from .views import CategoryViewSet


router = DefaultRouter()

router.register('category', CategoryViewSet)

urlpatterns = router.urls
