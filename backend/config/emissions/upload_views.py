import pandas as pd

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import (
    DataSource,
    EmissionRecord
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

        filename = csv_file.name.lower()

        # Detect source type

        if 'utility' in filename:
            source_type = 'UTILITY'

        elif 'travel' in filename:
            source_type = 'TRAVEL'

        else:
            source_type = 'SAP'

        # Create datasource

        data_source = DataSource.objects.create(
            source_type=source_type,
            file_name=csv_file.name
        )

        # Process rows

        for _, row in df.iterrows():

            activity = str(
                row.get('activity_type', 'Unknown')
            )

            quantity = float(
                row.get('quantity', 0)
            )

            unit = str(
                row.get('unit', 'Liters')
            )

            record_date = row.get('record_date')

            # Normalization logic

            if unit.lower() == 'gallons':

                normalized_quantity = quantity * 3.785
                normalized_unit = 'Liters'

            elif unit.lower() == 'mwh':

                normalized_quantity = quantity * 1000
                normalized_unit = 'kWh'

            else:

                normalized_quantity = quantity
                normalized_unit = unit

            # Suspicious detection

            suspicious = normalized_quantity > 10000

            # Save emission record

            EmissionRecord.objects.create(
                data_source=data_source,
                scope='SCOPE_1',
                activity_type=activity,
                quantity=quantity,
                unit=unit,
                normalized_quantity=normalized_quantity,
                normalized_unit=normalized_unit,
                record_date=record_date,
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