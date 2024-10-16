from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views as v

router = DefaultRouter()

router.register("products", v.ProductViewSet)
router.register("categories", v.CategoryViewSet)

urlpatterns = [
    path("", include(router.urls))
]