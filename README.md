# MovieLens DEA Pipeline — Streamlit Showcase

## Local Run
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Host on Streamlit Community Cloud (Free)

1. Push these files to a GitHub repo (public or private)
2. Go to https://share.streamlit.io
3. Click "New app" → connect your GitHub repo
4. Set Main file path: `app.py`
5. Click Deploy — live URL in ~2 minutes

## Files
- `app.py` — main Streamlit application
- `requirements.txt` — dependencies

## Pages
- Overview — KPIs, dataset summary, stack
- Architecture — Pipeline flow, Bronze/Silver/Gold layers, AWS services
- Preprocessing — 5-stage ETL pipeline with PySpark code
- Transformation — Schema evolution, key design decisions
- Athena & Gold Layer — SQL queries, output files
- Power BI Dashboard — Dashboard pages, colour system
- Challenges & Solutions — All 5 major challenges solved
- Key Insights — Analytical findings
