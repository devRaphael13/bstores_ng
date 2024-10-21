from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views as v

router = DefaultRouter()

router.register("products", v.ProductViewSet)
router.register("categories", v.CategoryViewSet)
router.register("sizes", v.SizeViewSet)
router.register("colours", v.ColourViewSet)
urlpatterns = [
    path("", include(router.urls))
]