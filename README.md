# USMLE Curriculum Mapper

This repository contains a Streamlit app that maps course/session PDFs to the USMLE Content Outline (Step 1 and Step 2 CK) and labels sentences by Physician Tasks/Competencies.

## Features
- PDF upload and extraction
- Learning Objectives detection
- Keyword + semantic matches (organ systems, Step 1/2 CK domains)
- Competency tagging (Diagnosis, Management, Foundational Science, etc.)
- Coverage rubric (Extensive / Moderate / Low)
- Downloadable Word + Excel reports

## Quickstart (Local)
```bash
pip install -r app/requirements.txt
python -c "import nltk; nltk.download('punkt')"
streamlit run app/app.py
```

## Deploy to Streamlit Community Cloud
1. Push this repo to GitHub.
2. Go to https://streamlit.io/cloud and deploy selecting `app/app.py` as the entry point.

## Data
Keyword sets are under `data/` and were derived from the official USMLE content outline and specifications.
