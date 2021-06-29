from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
# router.register('product', views.ProductViewSet, basename='product')


urlpatterns = [
    path('', include(router.urls)),
]