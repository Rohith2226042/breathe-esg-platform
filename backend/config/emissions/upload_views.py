import pandas as pd

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import (
    EmissionRecord,
    Organization,
    DataSource
)


@api_view(['POST'])
def upload_csv(request):

    csv_file = request.FILES.get('file')

    if not csv_file:
        return Response(
            {"error": "No file uploaded"},
            status=400
        )

    try:

        df = pd.read_csv(csv_file)

        # Create default organization
        organization, _ = Organization.objects.get_or_create(
            name="Demo Company"
        )

        # Create datasource record
        data_source = DataSource.objects.create(
            organization=organization,
            source_type='SAP',
            file_name=csv_file.name
        )

        for _, row in df.iterrows():

            # Handle multiple realistic column names
            activity = (
                row.get('Activity')
                or row.get('Fuel Type')
                or row.get('Material')
                or row.get('Description')
                or 'Unknown'
            )

            quantity = (
                row.get('Quantity')
                or row.get('Amount')
                or row.get('Volume')
                or 0
            )

            unit = (
                row.get('Unit')
                or row.get('UOM')
                or row.get('Measurement Unit')
                or 'Liters'
            )

            scope = (
                row.get('Scope')
                or 'SCOPE_1'
            )

            # Convert quantity safely
            try:
                quantity = float(quantity)
            except:
                quantity = 0

            # Suspicious logic
            suspicious = quantity > 10000

            EmissionRecord.objects.create(
                organization=organization,
                data_source=data_source,
                scope=scope,
                activity_type=str(activity),
                quantity=quantity,
                unit=str(unit),
                normalized_quantity=quantity,
                normalized_unit=str(unit),
                is_suspicious=suspicious,
                status='PENDING'
            )

        return Response({
            "message": "CSV uploaded successfully"
        })

    except Exception as e:

        return Response({
            "error": str(e)
        }, status=500)