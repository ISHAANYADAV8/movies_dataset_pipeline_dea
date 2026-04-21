# MovieLens DEA Pipeline — Streamlit Showcase

## Local Run
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Screenshot Setup (Important)
Place these 3 image files in the same folder as app.py:
  dashboard_page1.png   <- Page 1 "The Big Picture"
  dashboard_page2.png   <- Page 2 "Genre Intelligence"  
  dashboard_page3.png   <- Page 3 "What to Watch"

These files are included in the download bundle.
Without them the app still works with placeholder boxes.

## Host Free on Streamlit Community Cloud
1. Push all files (app.py + requirements.txt + 3 PNGs) to GitHub
2. Go to https://share.streamlit.io
3. New app -> connect repo -> Main file: app.py -> Deploy

## Pages
- Overview          : KPIs, dataset summary, tech stack
- Architecture      : Pipeline flow, 3-zone data lake, AWS services
- Preprocessing     : 5-stage ETL pipeline + full PySpark code
- Transformation    : Schema evolution, design decisions
- Athena & Gold     : All SQL queries, file structure
- Power BI Dashboard: All 3 screenshots + per-chart analysis + presentation tips
- Challenges        : 5 problems with Problem/Solution/Tag
- Key Insights      : 6 analytical findings + tech mastered grid
