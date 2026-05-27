# Breathe ESG Platform

An ESG emissions intelligence platform built using Django REST Framework, React, PostgreSQL, and cloud deployment infrastructure.

The platform ingests emissions-related CSV files from multiple enterprise systems, normalizes records, detects suspicious activities, and provides analyst review workflows.

---

# Features

## CSV Upload Pipeline

Supports ingestion from:
- SAP exports
- Utility provider exports
- Travel platform exports

---

## ESG Scope Classification

Automatically classifies records into:

| Scope | Description |
|---|---|
| Scope 1 | Direct fuel emissions |
| Scope 2 | Electricity emissions |
| Scope 3 | Travel and indirect emissions |

---

## Suspicious Activity Detection

Flags unusual records such as:
- Extremely high fuel usage
- Large electricity consumption
- Unusual travel activity

---

## Analyst Review Workflow

Analysts can:
- Approve records
- Reject records
- Add notes
- Review suspicious entries

---

## Dashboard Analytics

Dashboard includes:
- Total records
- Suspicious records
- Approved records
- Pending reviews
- Pie chart visualization

---

# Technology Stack

## Frontend
- React
- Vite
- Axios
- Recharts

## Backend
- Django
- Django REST Framework
- Pandas

## Database
- PostgreSQL

## Deployment
- Vercel (Frontend)
- Render (Backend + PostgreSQL)

---

# Architecture

Frontend communicates with Django REST APIs.

CSV files are uploaded through React UI and processed by backend ingestion services.

Processed data is normalized and stored in PostgreSQL.

---

# API Endpoints

## Upload CSV
POST /api/upload/

## Emission Records
GET /api/emissions/

## Approve Record
POST /api/emissions/{id}/approve/

## Reject Record
POST /api/emissions/{id}/reject/

---

# ESG Scope Mapping Logic

## Scope 1
Examples:
- Diesel Consumption
- Petrol Consumption
- Industrial Fuel Oil

## Scope 2
Examples:
- Electricity Usage
- Factory Electricity

## Scope 3
Examples:
- Business Flight
- Employee Travel

---

# Suspicious Detection Rules

Current rule-based thresholds:

| Activity Type | Threshold |
|---|---|
| Fuel Activities | > 10000 |
| Electricity Usage | High abnormal usage |
| Travel Records | Large travel values |

---

# Real-World ESG Research

The implementation was inspired by:
- SAP sustainability exports
- Utility billing systems
- Corporate travel platforms

Real-world ESG data commonly contains:
- inconsistent units
- missing values
- duplicate rows
- mixed naming conventions

The platform includes normalization logic to improve ingestion quality.

---

# PostgreSQL Migration

Initially developed using SQLite for local development.

Migrated to PostgreSQL for:
- production readiness
- scalability
- relational consistency

---

## PostgreSQL Architecture Rationale

The platform uses PostgreSQL as the primary production database.

Reasons for choosing PostgreSQL:

- Strong relational integrity
- Reliable transactional support
- Better scalability than SQLite
- Structured ESG record storage
- Efficient relationship handling between:
  - organizations
  - data sources
  - emission records

PostgreSQL also supports future scalability features such as:
- advanced ESG analytics
- partitioned historical data
- audit history tables
- large-scale ingestion pipelines

The relational schema allows:
- traceable ESG workflows
- analyst review tracking
- normalized emissions storage
- source-to-record lineage tracking


# Deployment Links

## Frontend
https://breathe-esg-platform-delta.vercel.app

## Backend
https://breathe-esg-platform-hmrs.onrender.com

---

# Future Improvements

- Machine learning anomaly detection
- Historical audit snapshots
- Authentication & RBAC
- Advanced ESG analytics
- Carbon conversion engine
- Batch processing pipelines

---

# Local Setup

## Backend

```bash
cd backend/config
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver