from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('avaliacoes', views.AvaliacaoViewSet)

urlpatterns = router.urls
