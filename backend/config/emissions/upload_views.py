import pandas as pd

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import EmissionRecord


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

        for _, row in df.iterrows():

            activity = str(row.get('Activity', 'Unknown'))

            quantity = float(row.get('Quantity', 0))

            unit = str(row.get('Unit', 'Liters'))

            suspicious = quantity > 10000

            EmissionRecord.objects.create(
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