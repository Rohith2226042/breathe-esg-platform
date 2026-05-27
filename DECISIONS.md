# Architecture Decisions

## Backend Framework Choice

Django REST Framework was selected because:

- Rapid API development
- Built-in admin support
- Strong ORM support
- Easy PostgreSQL integration
- Clean serializer architecture

Alternative considered:
- FastAPI

Reason not selected:
- Django provides stronger built-in admin/data tooling for ESG workflows.

---

## Database Choice

PostgreSQL was selected because:

- Production-grade relational database
- Strong structured data support
- Better scalability than SQLite
- Industry standard for analytics systems

Alternative considered:
- SQLite

Reason not selected:
- SQLite is suitable only for local development.

---

## Frontend Choice

React + Vite selected because:

- Fast development experience
- Simple component architecture
- Easy API integration
- Lightweight deployment on Vercel

---

## CSV Processing Strategy

CSV uploads are parsed using pandas.

Reason:
- Handles messy enterprise CSV formats better
- Easier normalization and cleaning
- Supports future transformations

---

## Suspicious Record Detection

Current suspicious detection rules:
- Fuel quantity > 10000
- High electricity usage
- Large travel values

Reason:
- Demonstrates anomaly detection workflow.

Future improvement:
- ML-based anomaly detection.

---

## ESG Scope Classification

Scope mapping rules:

### Scope 1
Fuel combustion activities.

### Scope 2
Electricity consumption.

### Scope 3
Travel and indirect emissions.

---

## Deployment Decisions

Frontend:
- Vercel

Backend:
- Render

Database:
- PostgreSQL on Render

Reason:
- Free deployment support
- Fast setup
- Cloud-hosted APIs

---

## Audit Tracking Design

Emission records store:
- status
- analyst_notes
- timestamps

Reason:
- Enables governance and compliance tracking.

## PostgreSQL Schema Design

The database schema was intentionally normalized into separate entities:

- Organization
- DataSource
- EmissionRecord

Reason:
- Avoid duplicate source metadata
- Improve scalability
- Support future multi-tenant ESG workflows
- Enable source-level auditability

Foreign key relationships help preserve:
- source lineage
- governance traceability
- ESG review workflows