from django.urls import path
from rest_framework.routers import DefaultRouter

from vehicle.apps import VehicleConfig
from vehicle.views import (CarAPIViewSet, MotoCreateAPIView, MotoListAPIView, MotoDetailAPIView, MotoUpdateAPIView,
                           MotoDeleteAPIView, MilageAPIViewSet, MotoMilageListAPIView)

app_name = VehicleConfig.name


router = DefaultRouter()
router.register('car', CarAPIViewSet, basename='car')
router.register('milage', MilageAPIViewSet, basename='milage')

urlpatterns = [
    path('moto/create/', MotoCreateAPIView.as_view(), name='moto-create'),
    path('moto/', MotoListAPIView.as_view(), name='moto-list'),
    path('moto/detail/<int:pk>/', MotoDetailAPIView.as_view(), name='moto-detail'),
    path('moto/update/<int:pk>/', MotoUpdateAPIView.as_view(), name='moto-update'),
    path('moto/delete/<int:pk>/', MotoDeleteAPIView.as_view(), name='moto-delete'),
    path('moto/milage/', MotoMilageListAPIView.as_view(), name='moto-milage'),
] + router.urls
