from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SensorViewSet, SensorDataViewSet


router = DefaultRouter()
router.register(r'sensors', SensorViewSet)
router.register(r'sensordata', SensorDataViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
