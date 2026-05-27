# Engineering Tradeoffs

## 1. Simplicity vs Accuracy

Decision:
Used rule-based suspicious detection instead of ML models.

Why:
- Faster implementation
- Easier debugging
- Easier demonstration during assessment

Tradeoff:
Less intelligent anomaly detection.

Future Improvement:
Machine learning anomaly scoring.

---

## 2. CSV Upload Flexibility vs Strict Validation

Decision:
Allow flexible CSV formats.

Why:
- Real enterprise files are inconsistent
- Easier testing with different ESG exports

Tradeoff:
Requires stronger normalization logic.

---

## 3. SQLite vs PostgreSQL

Decision:
Moved to PostgreSQL.

Why:
- Better production readiness
- Strong relational support
- Scalable architecture

Tradeoff:
Slightly more deployment complexity.

---

## 4. Frontend Simplicity vs Advanced UX

Decision:
Simple React dashboard UI.

Why:
- Faster delivery
- Clear ESG workflow visibility
- Easy reviewer interaction

Tradeoff:
Limited enterprise UX features.

Future Improvements:
- Pagination
- Advanced filtering
- Charts per source type
- Historical analytics

---

## 5. Scope Classification Rules

Decision:
Keyword-based ESG scope mapping.

Why:
- Easy to explain
- Easy to maintain
- Predictable behavior

Tradeoff:
Not fully dynamic.

Future Improvement:
Configurable ESG mapping engine.

---

## 6. Audit Tracking Design

Decision:
Track:
- status
- analyst_notes
- timestamps

Why:
- Lightweight governance support
- Demonstrates ESG review workflow

Tradeoff:
No complete historical version snapshots yet.

Future Improvement:
Full audit/version history tables.