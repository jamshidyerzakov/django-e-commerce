from rest_framework.routers import DefaultRouter

from .views import CartViewSet


router = DefaultRouter()

router.register('cart', CartViewSet)

urlpatterns = router.urls
