import pandas as pd

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import (
    Organization,
    DataSource,
    EmissionRecord
)


@api_view(['POST'])
def upload_csv(request):

    file = request.FILES.get('file')

    if not file:
        return Response({
            "error": "No file uploaded"
        }, status=400)

    df = pd.read_csv(file)

    organization, _ = Organization.objects.get_or_create(
        name="Breathe ESG Demo Org"
    )

    data_source = DataSource.objects.create(
        organization=organization,
        source_type='SAP',
        file_name=file.name
    )

    for _, row in df.iterrows():

        quantity = float(row['quantity'])

        suspicious = quantity > 10000

        EmissionRecord.objects.create(
            organization=organization,
            data_source=data_source,
            scope=row['scope'],
            activity_type=row['activity_type'],
            quantity=quantity,
            unit=row['unit'],
            normalized_quantity=quantity,
            normalized_unit=row['unit'],
            record_date=row['record_date'],
            is_suspicious=suspicious
        )

    return Response({
        "message": "CSV uploaded successfully"
    })