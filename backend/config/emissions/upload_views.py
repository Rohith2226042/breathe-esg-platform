import pandas as pd

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import (
    DataSource,
    EmissionRecord
)


# ==========================================
# EMISSION FACTORS
# ==========================================

EMISSION_FACTORS = {

    # SAP / Fuel
    'diesel': 2.68,
    'petrol': 2.31,
    'industrial fuel oil': 3.10,

    # Travel
    'flight': 0.15,
    'business flight': 0.18,

    # Utility
    'electricity': 0.40,
    'factory electricity': 0.45,
}


# ==========================================
# NORMALIZATION FUNCTION
# ==========================================

def calculate_emissions(activity, quantity):

    activity_lower = activity.lower()

    for keyword, factor in EMISSION_FACTORS.items():

        if keyword in activity_lower:

            return quantity * factor

    # fallback if unknown activity
    return quantity


# ==========================================
# SCOPE DETECTION
# ==========================================

def detect_scope(activity):

    activity_lower = activity.lower()

    if any(word in activity_lower for word in [
        'diesel',
        'petrol',
        'fuel',
        'oil'
    ]):
        return 'SCOPE_1'

    elif any(word in activity_lower for word in [
        'electricity'
    ]):
        return 'SCOPE_2'

    elif any(word in activity_lower for word in [
        'flight',
        'travel'
    ]):
        return 'SCOPE_3'

    return 'SCOPE_1'


# ==========================================
# SUSPICIOUS RECORD DETECTION
# ==========================================

def is_suspicious_record(quantity, normalized_quantity):

    if quantity > 10000:
        return True

    if normalized_quantity > 5000:
        return True

    return False


# ==========================================
# CSV INGESTION API
# ==========================================

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

        # ==========================================
        # SOURCE TYPE DETECTION
        # ==========================================

        if 'utility' in filename:
            source_type = 'UTILITY'

        elif 'travel' in filename:
            source_type = 'TRAVEL'

        else:
            source_type = 'SAP'

        data_source = DataSource.objects.create(
            source_type=source_type,
            file_name=csv_file.name
        )

        created_records = []

        # ==========================================
        # PROCESS EACH ROW
        # ==========================================

        for _, row in df.iterrows():

            activity = str(
                row.get('activity_type', 'Unknown')
            )

            quantity = float(
                row.get('quantity', 0)
            )

            unit = str(
                row.get('unit', 'Units')
            )

            record_date = row.get('record_date')

            # ==========================================
            # NORMALIZATION ENGINE
            # ==========================================

            normalized_quantity = calculate_emissions(
                activity,
                quantity
            )

            normalized_unit = 'kgCO2e'

            # ==========================================
            # SCOPE DETECTION
            # ==========================================

            scope = detect_scope(activity)

            # ==========================================
            # SUSPICIOUS DETECTION
            # ==========================================

            suspicious = is_suspicious_record(
                quantity,
                normalized_quantity
            )

            record = EmissionRecord.objects.create(
                data_source=data_source,
                scope=scope,
                activity_type=activity,
                quantity=quantity,
                unit=unit,
                normalized_quantity=normalized_quantity,
                normalized_unit=normalized_unit,
                record_date=record_date,
                is_suspicious=suspicious,
                status='PENDING'
            )

            created_records.append(record.id)

        return Response({
            "message": "CSV uploaded successfully",
            "source_type": source_type,
            "records_created": len(created_records)
        })

    except Exception as e:

        return Response({
            "error": str(e)
        }, status=500)