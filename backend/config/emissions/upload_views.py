
import pandas as pd
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.decorators import parser_classes
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import (
    Organization,
    DataSource,
    EmissionRecord
)


@api_view(['GET', 'POST'])
@parser_classes([MultiPartParser, FormParser])
def upload_csv(request):

    file = request.FILES.get('file')

    if not file:
        return Response({
            'error': 'No file uploaded'
        }, status=400)

    df = pd.read_csv(file)

    organization = Organization.objects.first()

    data_source = DataSource.objects.create(
        organization=organization,
        source_type='SAP',
        file_name=file.name
    )

    created_records = []

   for _, row in df.iterrows():

    quantity = float(row['quantity'])

    unit = row['unit']

    normalized_quantity = quantity
    normalized_unit = unit

    # Unit normalization

    if unit.lower() == "gallons":

        normalized_quantity = quantity * 3.78541
        normalized_unit = "Liters"

    elif unit.lower() == "kwh":

        normalized_quantity = quantity / 1000
        normalized_unit = "MWh"

    suspicious = normalized_quantity > 10000

    record = EmissionRecord.objects.create(
        organization=organization,
        data_source=data_source,
        scope='SCOPE_1',
        activity_type=row['activity_type'],
        quantity=quantity,
        unit=unit,
        normalized_quantity=normalized_quantity,
        normalized_unit=normalized_unit,
        record_date=row['record_date'],
        is_suspicious=suspicious,
        status='PENDING'
    )

    created_records.append(record.id)

    return Response({
        'message': 'CSV uploaded successfully',
        'records_created': created_records
    })