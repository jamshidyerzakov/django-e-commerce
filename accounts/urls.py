from accounts import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('user', views.UserViewSet)
router.register('seller', views.SellerViewSet)
router.register('customer', views.CustomerViewSet)
router.register('driver', views.DriverViewSet)
router.register('moderator', views.ModeratorViewSet)
router.register('admin', views.AdminViewSet)

urlpatterns = router.urls
