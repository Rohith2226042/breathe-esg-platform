# ESG Emissions Data Model

## Core Entities

### Organization
Represents a company or client uploading ESG data.

Fields:
- id
- name

---

### DataSource
Represents the source system of uploaded ESG data.

Supported sources:
- SAP
- Utility
- Travel

Fields:
- source_type
- file_name
- uploaded_at

---

### EmissionRecord
Represents normalized emissions activity records.

Fields:
- scope
- activity_type
- quantity
- unit
- normalized_quantity
- normalized_unit
- record_date
- is_suspicious
- status
- analyst_notes
- created_at

---

## Relationships

- One Organization can have many DataSources
- One DataSource can contain many EmissionRecords

---

## ESG Scope Mapping

### Scope 1
Direct emissions:
- Diesel
- Petrol
- Fuel Oil

### Scope 2
Indirect electricity emissions:
- Electricity Usage
- Factory Electricity

### Scope 3
Indirect travel emissions:
- Business Flight
- Employee Travel

---

## Suspicious Activity Rules

Records are flagged suspicious when:
- Fuel quantity > 10000 liters
- Electricity usage unusually high
- Travel distance unusually large

---

## Status Workflow

PENDING → APPROVED / REJECTED

Analysts can:
- approve records
- reject records
- add notes