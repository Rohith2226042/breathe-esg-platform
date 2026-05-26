from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    OrganizationViewSet,
    DataSourceViewSet,
    EmissionRecordViewSet
)

from .upload_views import upload_csv

router = DefaultRouter()

router.register(r'organizations', OrganizationViewSet)
router.register(r'datasources', DataSourceViewSet)
router.register(r'emissions', EmissionRecordViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('upload-csv/', upload_csv),
]