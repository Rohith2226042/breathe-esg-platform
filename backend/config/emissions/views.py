from django.utils.timezone import now

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import (
    Organization,
    DataSource,
    EmissionRecord
)

from .serializers import (
    OrganizationSerializer,
    DataSourceSerializer,
    EmissionRecordSerializer
)


class OrganizationViewSet(viewsets.ModelViewSet):

    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer


class DataSourceViewSet(viewsets.ModelViewSet):

    queryset = DataSource.objects.all()
    serializer_class = DataSourceSerializer


class EmissionRecordViewSet(viewsets.ModelViewSet):

    queryset = EmissionRecord.objects.all()
    serializer_class = EmissionRecordSerializer

    @action(detail=True, methods=['post'])
    def approve(self, request, pk=None):

        record = self.get_object()

        record.status = 'APPROVED'
        record.reviewed_at = now()

        record.save()

        return Response({
            "message": "Record approved"
        })

    @action(detail=True, methods=['post'])
    def reject(self, request, pk=None):

        record = self.get_object()

        record.status = 'REJECTED'
        record.reviewed_at = now()

        record.save()

        return Response({
            "message": "Record rejected"
        })