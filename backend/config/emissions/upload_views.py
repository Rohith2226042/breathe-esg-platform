import pandas as pd

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import DataSource, EmissionRecord


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

        data_source = DataSource.objects.create(
            source_type='SAP',
            file_name=csv_file.name
        )

        for _, row in df.iterrows():

            activity = str(
                row.get('Activity')
                or row.get('Fuel Type')
                or row.get('Description')
                or row.get('Category')
                or 'Unknown'
            )

            quantity = float(
                row.get('Quantity')
                or row.get('Amount')
                or row.get('Liters')
                or row.get('Value')
                or 0
            )

            unit = str(
                row.get('Unit')
                or row.get('UOM')
                or 'Liters'
            )

            suspicious = quantity > 10000

            EmissionRecord.objects.create(
                data_source=data_source,
                scope='SCOPE_1',
                activity_type=activity,
                quantity=quantity,
                unit=unit,
                normalized_quantity=quantity,
                normalized_unit=unit,
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