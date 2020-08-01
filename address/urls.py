from rest_framework.routers import DefaultRouter
from .views import CustomerAddressViewSet, SellerAddressViewSet

router = DefaultRouter()

router.register('seller-address', SellerAddressViewSet)
router.register('customer-address', CustomerAddressViewSet)

urlpatterns = router.urls
