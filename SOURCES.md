# Real-World ESG Data Source Research

## SAP ERP Exports

Typical SAP sustainability exports contain:

- Fuel consumption
- Material usage
- Industrial production data
- Emissions activity logs

Common formats:
- CSV
- Excel
- ERP extracts

Example activities:
- Diesel Consumption
- Petrol Consumption
- Industrial Fuel Oil

Mapped to:
- Scope 1 emissions

---

## Utility Provider Data

Utility systems usually provide:

- Electricity consumption
- Meter readings
- Monthly usage statements

Common formats:
- CSV
- PDF bills
- Excel reports

Example activities:
- Electricity Usage
- Factory Electricity

Mapped to:
- Scope 2 emissions

---

## Corporate Travel Platforms

Travel systems contain:

- Flight bookings
- Hotel stays
- Employee travel logs

Common providers:
- SAP Concur
- Navan
- TravelPerk

Example activities:
- Business Flight
- Employee Travel

Mapped to:
- Scope 3 emissions

---

## Data Quality Problems Observed

Real ESG systems commonly contain:

- Missing values
- Different unit formats
- Duplicate rows
- Incorrect dates
- Mixed naming conventions

Examples:
- liters vs Liters
- diesel vs Diesel Consumption

---

## Normalization Strategy

The platform normalizes:
- activity names
- units
- scopes
- suspicious thresholds

Examples:
- Electricity activities → Scope 2
- Travel activities → Scope 3
- Fuel activities → Scope 1

---

## Suspicious Activity Detection

Examples:
- Extremely high fuel usage
- Unusually large electricity values
- Travel anomalies

Purpose:
- Assist ESG analysts during review workflows.