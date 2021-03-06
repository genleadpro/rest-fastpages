from . import views
from rest_framework import routers


router = routers.DefaultRouter()

router.register(r'users', views.UserViewSet)
router.register(r'clients', views.ClientViewSet)
router.register(r'pages', views.PageViewSet)
router.register(r'orders', views.OrderViewSet)

api_urlpatterns = router.urls
