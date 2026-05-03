# KiranaLens

KiranaLens is a system for remote credit underwriting of small retail stores using computer vision and geospatial data. It estimates store inventory and local demand to generate a credit recommendation with an associated confidence score.

---

## Problem

* Small retail stores often operate without digital financial records
* Traditional credit assessment requires manual field audits
* Lack of reliable data increases lending risk

---

## Approach

The system combines two primary signals:

* Visual estimation of inventory from shelf images
* Geospatial estimation of market demand based on nearby retail activity

These signals are validated and used to compute a risk-aware credit decision.

---

## System Components

**Vision Engine**
Processes store images and estimates a Shelf Density Index (SDI) using object detection.

**Geo Engine**
Retrieves nearby retail density using OpenStreetMap (Overpass API) to estimate demand.

**Fraud Engine**
Checks consistency between inventory and demand signals.

**Decision Engine**
Calculates recommended credit limit and confidence score based on signal agreement.

---

## Pipeline

Images → Vision → SDI
Location → Geo → Demand
→ Validation → Decision

---

## Installation

```bash
pip install -r requirements.txt
```

---

## Usage

```bash
streamlit run main.py
```

---

## Output

* Recommended credit limit
* Confidence score
* Decision (Approve / Verify)
* Explanation of decision factors

---

## Dependencies

* streamlit
* ultralytics
* opencv-python
* numpy
* requests

---

## Notes

* Internet connection is required for geospatial queries
* System includes fallback logic if API is unavailable

---

## Context

Developed for TenzorX 2026 – Problem Statement 4
