from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import EmissionRecordViewSet
from .upload_views import upload_csv

router = DefaultRouter()

router.register(
    r'emissions',
    EmissionRecordViewSet,
    basename='emissions'
)

urlpatterns = [

    path('', include(router.urls)),

    path(
        'upload-csv/',
        upload_csv,
        name='upload-csv'
    ),
]