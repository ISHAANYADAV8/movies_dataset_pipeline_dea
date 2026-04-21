import streamlit as st
import base64
import os

st.set_page_config(
    page_title="MovieLens DEA Pipeline",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ─── Helper: load image as base64 ────────────────────────────────────────────
def img_b64(filename):
    candidates = [
        filename,
        os.path.join(os.path.dirname(__file__), filename),
        os.path.join(os.path.dirname(__file__), os.path.basename(filename)),
    ]
    for p in candidates:
        if os.path.exists(p):
            with open(p, "rb") as f:
                return base64.b64encode(f.read()).decode()
    return None

def show_screenshot(filename, label):
    b64 = img_b64(filename)
    if b64:
        st.markdown(f"""
        <div class='screenshot-wrap'>
            <img src='data:image/png;base64,{b64}' alt='{label}'/>
            <div class='screenshot-label'>📊 {label}</div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.info(f"📷 Screenshot `{filename}` not found — place it alongside app.py to display it here.")

def chart_card(chart_type, css_class, name, desc, insight=None):
    insight_html = f"<div class='ca-insight'><b>💬 Presentation tip:</b> {insight}</div>" if insight else ""
    st.markdown(f"""
    <div class='chart-analysis'>
        <div class='ca-header'>
            <span class='ca-type {css_class}'>{chart_type}</span>
            <span class='ca-name'>{name}</span>
        </div>
        <div class='ca-desc'>{desc}</div>
        {insight_html}
    </div>
    """, unsafe_allow_html=True)

# ─── CSS ─────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=DM+Sans:wght@300;400;500;600&display=swap');
:root {
    --bg:#0F1923; --surface:#1A2535; --surface2:#1E2D40;
    --gold:#E8B84B; --teal:#2E86AB; --green:#3BB273; --red:#E84855;
    --text:#F0F4F8; --muted:#8899AA; --border:#243347;
}
html,body,[data-testid="stAppViewContainer"]{background-color:var(--bg)!important;color:var(--text)!important;font-family:'DM Sans',sans-serif;}
[data-testid="stSidebar"]{background-color:var(--surface)!important;border-right:1px solid var(--border);}
[data-testid="stSidebar"] *{color:var(--text)!important;}
h1,h2,h3,h4{font-family:'Space Mono',monospace!important;color:var(--gold)!important;}
.stMarkdown p{color:var(--text);line-height:1.7;}
.card{background:var(--surface);border:1px solid var(--border);border-radius:12px;padding:22px 24px;margin-bottom:14px;}
.card-gold{border-left:4px solid var(--gold);} .card-teal{border-left:4px solid var(--teal);}
.card-green{border-left:4px solid var(--green);} .card-red{border-left:4px solid var(--red);}
.kpi-row{display:flex;gap:14px;flex-wrap:wrap;margin:20px 0;}
.kpi{background:var(--surface);border:1px solid var(--border);border-radius:10px;padding:18px 24px;flex:1;min-width:150px;text-align:center;}
.kpi .num{font-family:'Space Mono',monospace;font-size:1.9rem;color:var(--gold);}
.kpi .lbl{font-size:0.75rem;color:var(--muted);margin-top:4px;text-transform:uppercase;letter-spacing:1px;}
.pipeline{display:flex;align-items:center;overflow-x:auto;padding:20px 0;margin:16px 0;gap:0;}
.pipe-step{background:var(--surface2);border:1px solid var(--border);border-radius:10px;padding:14px 18px;text-align:center;min-width:110px;}
.pipe-step .icon{font-size:1.6rem;} .pipe-step .name{font-family:'Space Mono',monospace;font-size:0.68rem;color:var(--gold);margin-top:5px;}
.pipe-step .sub{font-size:0.62rem;color:var(--muted);margin-top:2px;}
.pipe-arrow{color:var(--gold);font-size:1.4rem;padding:0 6px;flex-shrink:0;}
.badge{display:inline-block;padding:3px 11px;border-radius:20px;font-size:0.7rem;font-family:'Space Mono',monospace;font-weight:700;text-transform:uppercase;letter-spacing:1px;margin-right:5px;}
.badge-bronze{background:#3D2B1A;color:#CD7F32;border:1px solid #CD7F32;}
.badge-silver{background:#1E2535;color:#C0C0C0;border:1px solid #C0C0C0;}
.badge-gold{background:#2A2210;color:var(--gold);border:1px solid var(--gold);}
.stage{background:var(--surface2);border-radius:10px;padding:16px 20px;margin-bottom:10px;border:1px solid var(--border);position:relative;}
.stage-num{position:absolute;top:-10px;left:14px;background:var(--gold);color:var(--bg);font-family:'Space Mono',monospace;font-size:0.68rem;font-weight:700;padding:2px 10px;border-radius:20px;}
.stage h4{color:var(--text)!important;font-size:0.93rem!important;margin:8px 0 5px 0;}
.stage li{font-size:0.86rem;color:var(--muted);line-height:1.6;margin-bottom:4px;}
.challenge{display:flex;gap:14px;background:var(--surface2);border-radius:10px;padding:16px 18px;margin-bottom:10px;border:1px solid var(--border);align-items:flex-start;}
.challenge .icon{font-size:1.4rem;flex-shrink:0;margin-top:2px;}
.challenge .ctitle{font-family:'Space Mono',monospace;font-size:0.82rem;color:var(--red);}
.challenge .sol{font-size:0.83rem;color:var(--text);margin-top:4px;line-height:1.6;}
.challenge .tag{display:inline-block;background:#1A3020;color:var(--green);border-radius:4px;font-size:0.68rem;padding:2px 8px;margin-top:6px;}
.tech-grid{display:flex;flex-wrap:wrap;gap:10px;margin:14px 0;}
.tech-item{background:var(--surface2);border:1px solid var(--border);border-radius:8px;padding:12px 14px;min-width:130px;flex:1;text-align:center;}
.tech-item .t-icon{font-size:1.5rem;} .tech-item .t-name{font-family:'Space Mono',monospace;font-size:0.7rem;color:var(--gold);margin-top:5px;}
.tech-item .t-role{font-size:0.67rem;color:var(--muted);margin-top:2px;}
.hero{background:linear-gradient(135deg,#1A2535 0%,#0F1923 60%);border:1px solid var(--border);border-radius:16px;padding:36px 44px;margin-bottom:26px;position:relative;overflow:hidden;}
.hero::before{content:'';position:absolute;top:0;right:0;width:280px;height:100%;background:radial-gradient(circle at 80% 50%,rgba(232,184,75,0.07) 0%,transparent 70%);}
.hero h1{font-size:1.9rem!important;margin:0 0 7px 0!important;}
.hero .sub{color:var(--muted);font-size:0.95rem;}
.hero .authors{margin-top:18px;display:flex;gap:16px;flex-wrap:wrap;}
.author-chip{background:var(--surface2);border:1px solid var(--border);border-radius:8px;padding:7px 14px;font-size:0.8rem;}
.author-chip span{color:var(--gold);font-family:'Space Mono',monospace;}
.screenshot-wrap{background:var(--surface2);border:1px solid var(--border);border-radius:12px;overflow:hidden;margin:14px 0;}
.screenshot-wrap img{width:100%;display:block;}
.screenshot-label{padding:10px 16px;background:var(--surface);border-top:1px solid var(--border);font-family:'Space Mono',monospace;font-size:0.72rem;color:var(--muted);}
.chart-analysis{background:var(--surface2);border:1px solid var(--border);border-radius:10px;padding:16px 20px;margin-bottom:10px;}
.chart-analysis .ca-header{display:flex;align-items:center;gap:8px;margin-bottom:8px;}
.chart-analysis .ca-type{font-size:0.68rem;font-family:'Space Mono',monospace;font-weight:700;padding:2px 8px;border-radius:20px;text-transform:uppercase;}
.ca-kpi{background:#dbeafe33;color:#60a5fa;border:1px solid #60a5fa55;}
.ca-bar{background:#d1fae533;color:#34d399;border:1px solid #34d39955;}
.ca-donut{background:#fef3c733;color:#fbbf24;border:1px solid #fbbf2455;}
.ca-scatter{background:#ede9fe33;color:#a78bfa;border:1px solid #a78bfa55;}
.ca-table{background:#fce7f333;color:#f472b6;border:1px solid #f472b655;}
.ca-heatmap{background:#fee2e233;color:#f87171;border:1px solid #f8717155;}
.ca-slicer{background:#ecfdf533;color:#4ade80;border:1px solid #4ade8055;}
.chart-analysis .ca-name{font-size:0.9rem;font-weight:600;color:var(--text);}
.chart-analysis .ca-desc{font-size:0.84rem;color:var(--muted);line-height:1.65;}
.chart-analysis .ca-insight{margin-top:10px;padding:8px 12px;background:var(--surface);border-left:3px solid var(--gold);border-radius:0 6px 6px 0;font-size:0.8rem;color:var(--muted);}
.chart-analysis .ca-insight b{color:var(--gold);}
.page-tab{border-radius:10px;padding:12px 18px;margin-bottom:18px;display:flex;align-items:center;gap:12px;}
.pt-1{background:linear-gradient(90deg,#1a5fa8 0%,#1a3550 100%);}
.pt-2{background:linear-gradient(90deg,#2e7d5e 0%,#1a3530 100%);}
.pt-3{background:linear-gradient(90deg,#7c3a7c 0%,#2a1a35 100%);}
.page-tab .pt-num{font-family:'Space Mono',monospace;font-size:0.7rem;padding:2px 10px;border-radius:20px;background:rgba(255,255,255,0.2);color:#fff;}
.page-tab .pt-title{font-family:'Space Mono',monospace;font-size:1rem;color:#fff;}
::-webkit-scrollbar{width:5px;height:5px;}
::-webkit-scrollbar-track{background:var(--bg);}
::-webkit-scrollbar-thumb{background:var(--border);border-radius:3px;}
[data-testid="metric-container"]{background:var(--surface)!important;border:1px solid var(--border)!important;border-radius:10px!important;padding:14px!important;}
[data-testid="stExpander"]{background:var(--surface2)!important;border:1px solid var(--border)!important;border-radius:8px!important;}
[data-baseweb="tab-list"]{background:var(--surface)!important;border-radius:8px;}
[aria-selected="true"]{color:var(--gold)!important;border-bottom-color:var(--gold)!important;}
</style>
""", unsafe_allow_html=True)

# ─── Sidebar ──────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style='padding:8px 0 18px 0;'>
        <div style='font-family:Space Mono,monospace;font-size:1.05rem;color:#E8B84B;'>🎬 MovieLens DEA</div>
        <div style='font-size:0.7rem;color:#8899AA;margin-top:3px;'>Data Engineering & Analytics Pipeline</div>
    </div>
    """, unsafe_allow_html=True)
    page = st.radio("Navigate", [
        "🏠  Overview","🏗️  Architecture","⚙️  Preprocessing",
        "🔄  Transformation","🗄️  Athena & Gold Layer",
        "📊  Power BI Dashboard","⚡  Challenges & Solutions","💡  Key Insights",
    ], label_visibility="collapsed")
    st.markdown("<hr style='border-color:#243347;margin:18px 0;'>", unsafe_allow_html=True)
    st.markdown("""
    <div style='font-size:0.7rem;color:#8899AA;'>
        <div style='margin-bottom:5px;'><span style='color:#E8B84B;'>▸</span> Parth Bisht · 23/IT/117</div>
        <div><span style='color:#E8B84B;'>▸</span> Ishaan Yadav · 23/IT/73</div>
    </div>
    """, unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
if "Overview" in page:
    st.markdown("""
    <div class='hero'>
        <h1>MOVIELENS INTELLIGENCE PIPELINE</h1>
        <div class='sub'>End-to-End Data Engineering & Analytics on AWS with Power BI Visualisation</div>
        <div class='authors'>
            <div class='author-chip'><span>Parth Bisht</span> · Roll No: 23/IT/117</div>
            <div class='author-chip'><span>Ishaan Yadav</span> · Roll No: 23/IT/73</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    <div class='kpi-row'>
        <div class='kpi'><div class='num'>20M+</div><div class='lbl'>Total Ratings</div></div>
        <div class='kpi'><div class='num'>27K</div><div class='lbl'>Movies</div></div>
        <div class='kpi'><div class='num'>138K</div><div class='lbl'>Users</div></div>
        <div class='kpi'><div class='num'>3</div><div class='lbl'>AWS Layers</div></div>
        <div class='kpi'><div class='num'>2m 36s</div><div class='lbl'>ETL Run Time</div></div>
        <div class='kpi'><div class='num'>3</div><div class='lbl'>BI Pages</div></div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("### Project Overview")
    st.markdown("""
    <div class='card card-teal'>
    <p>This project demonstrates an <b style='color:#F0F4F8;'>end-to-end cloud-based Data Engineering and Analytics (DEA) pipeline</b>
    built entirely on Amazon Web Services. The pipeline ingests a large-scale real-world movies dataset,
    transforms and enriches it using distributed PySpark computing, and delivers analytical insights through
    an interactive 3-page Power BI dashboard.</p>
    <p>The architecture follows an industry-standard <b style='color:#E8B84B;'>Bronze → Silver → Gold lakehouse pattern</b>,
    ensuring data quality, traceability, and clean separation of concerns across every stage.</p>
    </div>
    """, unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("#### 📦 Dataset")
        st.markdown("""
        <div class='card'>
        <div><span class='badge badge-gold'>Source</span> MovieLens 20M · GroupLens Research, UMN</div>
        <div style='margin-top:12px;font-size:0.84rem;color:#8899AA;'>
            <div style='margin-bottom:5px;'>📄 <b style='color:#F0F4F8;'>movies.csv</b> — movieId, title, genres</div>
            <div style='margin-bottom:5px;'>⭐ <b style='color:#F0F4F8;'>ratings.csv</b> — userId, movieId, rating, timestamp (20M rows)</div>
            <div>🏷️ <b style='color:#F0F4F8;'>tags.csv</b> — userId, movieId, tag, timestamp</div>
        </div>
        </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown("#### 🛠️ Tech Stack")
        st.markdown("""
        <div class='tech-grid'>
            <div class='tech-item'><div class='t-icon'>🪣</div><div class='t-name'>Amazon S3</div><div class='t-role'>Data Lake</div></div>
            <div class='tech-item'><div class='t-icon'>⚙️</div><div class='t-name'>AWS Glue</div><div class='t-role'>ETL · PySpark</div></div>
            <div class='tech-item'><div class='t-icon'>🔍</div><div class='t-name'>Athena</div><div class='t-role'>SQL Query Layer</div></div>
            <div class='tech-item'><div class='t-icon'>📊</div><div class='t-name'>Power BI</div><div class='t-role'>3-Page Dashboard</div></div>
        </div>
        """, unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
elif "Architecture" in page:
    st.markdown("# 🏗️ AWS Architecture")
    st.markdown("### Full Pipeline Flow")
    st.markdown("""
    <div class='pipeline'>
        <div class='pipe-step'><div class='icon'>📄</div><div class='name'>RAW CSVs</div><div class='sub'>Kaggle</div></div>
        <div class='pipe-arrow'>→</div>
        <div class='pipe-step' style='border-color:#CD7F32;'><div class='icon'>🪣</div><div class='name'>BRONZE</div><div class='sub'>S3 · Immutable</div></div>
        <div class='pipe-arrow'>→</div>
        <div class='pipe-step'><div class='icon'>🕷️</div><div class='name'>GLUE CRAWLER</div><div class='sub'>Schema Discovery</div></div>
        <div class='pipe-arrow'>→</div>
        <div class='pipe-step'><div class='icon'>⚙️</div><div class='name'>GLUE ETL</div><div class='sub'>PySpark</div></div>
        <div class='pipe-arrow'>→</div>
        <div class='pipe-step' style='border-color:#C0C0C0;'><div class='icon'>🪣</div><div class='name'>SILVER</div><div class='sub'>S3 · Processed</div></div>
        <div class='pipe-arrow'>→</div>
        <div class='pipe-step'><div class='icon'>🔍</div><div class='name'>ATHENA SQL</div><div class='sub'>Serverless</div></div>
        <div class='pipe-arrow'>→</div>
        <div class='pipe-step' style='border-color:#E8B84B;'><div class='icon'>🪣</div><div class='name'>GOLD</div><div class='sub'>S3 · CSVs</div></div>
        <div class='pipe-arrow'>→</div>
        <div class='pipe-step'><div class='icon'>📊</div><div class='name'>POWER BI</div><div class='sub'>Dashboard</div></div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("### Three-Zone Data Lake")
    c1, c2, c3 = st.columns(3)
    for col_el, badge_cls, badge_lbl, bucket, desc, files in [
        (c1, "badge-bronze", "BRONZE", "anime-bronze-aadi-2026",
         "Raw Zone — <b style='color:#F0F4F8;'>Immutable source of truth.</b><br>No transformations ever applied here.",
         ["raw/movies/movies.csv","raw/ratings/ratings.csv","raw/tags/tags.csv"]),
        (c2, "badge-silver", "SILVER", "anime-silver-aadi-2026",
         "Processed Zone — Output of Glue ETL.<br>Cleaned, joined, feature-engineered.",
         ["enriched_movies/","genre_analytics/","year_analytics/"]),
        (c3, "badge-gold", "GOLD", "anime-gold-aadi-2026",
         "Analytics Zone — Athena query results.<br>Dashboard-ready CSVs loaded into Power BI.",
         ["athena-results/","214feae7-....csv","(UUID-named by Athena)"]),
    ]:
        border_color = {"badge-bronze":"#CD7F32","badge-silver":"#C0C0C0","badge-gold":"#E8B84B"}[badge_cls]
        files_html = "".join([f"<code style='background:#0A1018;padding:2px 6px;border-radius:4px;font-size:0.73rem;display:block;margin-bottom:4px;'>{f}</code>" for f in files])
        with col_el:
            st.markdown(f"""
            <div class='card' style='border-top:3px solid {border_color};'>
                <span class='badge {badge_cls}'>{badge_lbl}</span>
                <div style='font-family:Space Mono,monospace;font-size:0.78rem;color:#F0F4F8;margin:12px 0 6px 0;'>{bucket}</div>
                <div style='font-size:0.82rem;color:#8899AA;line-height:1.8;margin-bottom:10px;'>{desc}</div>
                {files_html}
            </div>
            """, unsafe_allow_html=True)
    st.markdown("### AWS Services Used")
    for icon, name, desc in [
        ("🪣","Amazon S3","Three-zone data lake: Bronze (raw), Silver (processed), Gold (analytics results)"),
        ("🕷️","Glue Crawler","Auto-infers schema from raw CSVs, creates tables in Glue Data Catalog"),
        ("⚙️","Glue ETL Job","PySpark-based transformation — sampling, join, aggregation, feature engineering"),
        ("📚","Glue Data Catalog","Metadata store — holds table definitions for movie_db and all processed tables"),
        ("🔍","Amazon Athena","Serverless SQL engine to query processed S3 data and produce Gold layer CSVs"),
        ("🔐","AWS IAM","GlueS3Role-Aadi — grants Glue full S3 and Glue service permissions"),
    ]:
        st.markdown(f"""
        <div class='challenge'><div class='icon'>{icon}</div>
        <div><div class='ctitle'>{name}</div><div class='sol'>{desc}</div></div></div>
        """, unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
elif "Preprocessing" in page:
    st.markdown("# ⚙️ Data Preprocessing Pipeline")
    st.markdown("""
    <div class='card card-gold'>
    <p>The Glue ETL job executed a <b style='color:#E8B84B;'>5-stage preprocessing pipeline in PySpark</b>,
    reading directly from Bronze S3 paths and writing structured CSVs to the Silver layer.
    Each stage had a deliberate purpose — a structured data engineering workflow, not a monolithic script.</p>
    </div>
    """, unsafe_allow_html=True)
    stages = [
        ("Stage 1","🧹 Cleaning",[
            "<b>Type casting:</b> movieId → INT, rating → DOUBLE from raw strings",
            "<b>Null strategy:</b> LEFT JOIN used to retain movies with no ratings — avg_rating stored as NULL, preserving completeness rather than silently dropping unrated movies",
            "<b>Philosophy:</b> Never destroy data at the source — Bronze layer remains fully intact",
        ]),
        ("Stage 2","✂️ Pruning / Sampling",[
            "<b>Problem:</b> ratings.csv had 20 million rows — unprocessable with 2 Glue workers at full scale",
            "<b>Solution:</b> 10% random sample applied BEFORE any JOIN",
            "<code>df_ratings_sample = df_ratings.sample(fraction=0.1, seed=42)</code>",
            "<b>Statistical validity:</b> ~120K of 138K users · ~25K of 27K movies retained — aggregated metrics are statistically indistinguishable from full data",
            "<b>Seed=42:</b> fixed seed guarantees full reproducibility",
        ]),
        ("Stage 3","🔄 Transformation (Join)",[
            "Aggregation computed on ratings <b>BEFORE</b> the join — key optimisation",
            "Per-movie avg_rating and total_ratings computed first: 2M rows → 27K movie-level rows",
            "movies.csv LEFT JOINed against this compact 27K-row result on movieId",
            "tags.csv ingested to Bronze for future use but excluded from core ETL join",
        ]),
        ("Stage 4","🔧 Feature Engineering",[
            "<b>Year extraction:</b> regex on title field → 4-digit year from brackets",
            "Example: <code>'Toy Story (1995)'</code> → <code>year = 1995</code> as INT",
            "<b>Genre explosion:</b> pipe-delimited genre strings → individual rows",
            "Example: <code>'Adventure|Children|Fantasy'</code> → 3 rows per movie",
        ]),
        ("Stage 5","📦 Aggregation & Output",[
            "<b>Genre-level:</b> GROUP BY genre → avg_genre_rating, movie_count → genre_analytics/",
            "<b>Year-level:</b> GROUP BY year → movies_per_year, avg_rating_by_year → year_analytics/",
            "Pre-aggregating at ETL time reduces Athena compute costs significantly",
            "Three CSV datasets written to Silver with Spark's distributed write",
        ]),
    ]
    for num, title, bullets in stages:
        with st.expander(title, expanded=True):
            html = f"<div class='stage'><div class='stage-num'>{num}</div><h4>{title}</h4><ul style='margin:0;padding-left:18px;'>"
            for b in bullets:
                html += f"<li style='margin-bottom:5px;'>{b}</li>"
            html += "</ul></div>"
            st.markdown(html, unsafe_allow_html=True)
    st.markdown("### Transformation Summary")
    import pandas as pd
    df = pd.DataFrame([
        ("Type Casting","movieId → INT, rating → DOUBLE"),
        ("Statistical Sampling","10% random sample (seed=42): 20M → ~2M rows"),
        ("Aggregation-Before-Join","Per-movie avg_rating computed before join — 10x smaller"),
        ("Relational Join","movies.csv LEFT JOIN aggregated ratings on movieId"),
        ("Year Extraction","Regex: 'Toy Story (1995)' → year = 1995"),
        ("Genre Explosion","'Adventure|Children|Fantasy' → 3 genre rows"),
        ("Null Handling","Left join preserves movies with no ratings (NULL retained)"),
        ("Pre-Aggregation","Genre + year GROUP BYs computed at ETL time"),
    ], columns=["Stage","What Was Done"])
    st.dataframe(df, use_container_width=True, hide_index=True)
    st.markdown("### PySpark Code — Core ETL Logic")
    st.code("""
# Stage 2: Pruning ──────────────────────────────────────────────────────────
df_ratings = spark.read.csv("s3://anime-bronze-aadi-2026/raw/ratings/", header=True)
df_ratings_sample = df_ratings.sample(fraction=0.1, seed=42)  # 20M → ~2M

# Stage 3: Aggregate BEFORE join ────────────────────────────────────────────
from pyspark.sql.functions import avg, count, col, regexp_extract, explode, split

df_agg = df_ratings_sample.groupBy("movieId").agg(
    avg("rating").alias("avg_rating"),
    count("rating").alias("total_ratings")
)  # 27K rows — massively smaller than 2M

df_movies = spark.read.csv("s3://anime-bronze-aadi-2026/raw/movies/", header=True)
df_enriched = df_movies.join(df_agg, on="movieId", how="left")

# Stage 4: Feature Engineering ──────────────────────────────────────────────
df_enriched = df_enriched.withColumn(
    "year", regexp_extract(col("title"), r"\\((\\d{4})\\)", 1).cast("int")
)
df_exploded = df_enriched.withColumn(
    "genre", explode(split(col("genres"), "\\\\|"))
)

# Stage 5: Pre-Aggregation & Write ──────────────────────────────────────────
df_exploded.groupBy("genre").agg(
    avg("avg_rating").alias("avg_genre_rating"), count("movieId").alias("movie_count")
).write.csv("s3://anime-silver-aadi-2026/movie-analytics/genre_analytics/", header=True)

df_enriched.groupBy("year").agg(
    count("movieId").alias("movies_per_year"), avg("avg_rating").alias("avg_rating_by_year")
).write.csv("s3://anime-silver-aadi-2026/movie-analytics/year_analytics/", header=True)

df_enriched.write.csv("s3://anime-silver-aadi-2026/movie-analytics/enriched_movies/", header=True)
    """, language="python")

# ═══════════════════════════════════════════════════════════════════════════════
elif "Transformation" in page:
    st.markdown("# 🔄 Data Transformation — Structure & Schema")
    st.markdown("### Schema Evolution")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("<span class='badge badge-bronze'>BRONZE SCHEMA</span>", unsafe_allow_html=True)
        st.code("""movies.csv
movieId   STRING  (raw)
title     STRING  "Toy Story (1995)"
genres    STRING  "Adventure|Animation"

ratings.csv
userId    STRING
movieId   STRING
rating    STRING  (needs cast)
timestamp STRING""", language="text")
    with c2:
        st.markdown("<span class='badge badge-silver'>SILVER SCHEMA</span>", unsafe_allow_html=True)
        st.code("""enriched_movies/
movieId       INT      ← cast
title         STRING
genres        STRING
genre         STRING   ← EXPLODED
avg_rating    DOUBLE   ← DERIVED
total_ratings BIGINT   ← DERIVED
year          INT      ← EXTRACTED

genre_analytics/
genre, avg_genre_rating, movie_count

year_analytics/
year, movies_per_year, avg_rating_by_year""", language="text")
    st.markdown("### Key Design Decisions")
    for icon, title, desc, tag in [
        ("🎯","Aggregate Before Join",
         "Standard ETL joins first (20M × 27K), then aggregates. We reversed this — aggregate to 27K rows FIRST, then join. A 10x reduction in intermediate data size.",
         "Performance Optimisation"),
        ("🔗","LEFT JOIN over INNER JOIN",
         "INNER JOIN would silently drop movies with zero ratings, distorting genre counts and catalog completeness. LEFT JOIN preserves all 27K movies with NULL avg_rating where needed.",
         "Data Integrity"),
        ("💥","Genre Explosion (1→N rows)",
         "Pipe-delimited genres stored as one row can't be aggregated by genre. Exploding into separate rows enables GROUP BY genre queries — deliberate schema denormalisation for analytics.",
         "Analytical Design"),
        ("📅","Year as Extracted INT Column",
         "Storing year as INT rather than extracting at query time means every Athena query gets a fast integer filter instead of a slow per-row regex match.",
         "Query Performance"),
    ]:
        st.markdown(f"""
        <div class='challenge'><div class='icon'>{icon}</div>
        <div><div class='ctitle'>{title}</div><div class='sol'>{desc}</div>
        <span class='tag'>{tag}</span></div></div>
        """, unsafe_allow_html=True)
    import pandas as pd
    st.markdown("### Output Tables — Silver Layer")
    st.dataframe(pd.DataFrame([
        ("enriched_movies","movie-analytics/enriched_movies/","movieId, title, genres, genre, avg_rating, total_ratings, year","~27K rows"),
        ("genre_analytics","movie-analytics/genre_analytics/","genre, avg_genre_rating, movie_count","~20 rows"),
        ("year_analytics","movie-analytics/year_analytics/","year, movies_per_year, avg_rating_by_year","~50 rows"),
    ], columns=["Table","S3 Path","Fields","Approx Rows"]), use_container_width=True, hide_index=True)

# ═══════════════════════════════════════════════════════════════════════════════
elif "Athena" in page:
    st.markdown("# 🗄️ Athena Query Layer — Silver → Gold")
    st.markdown("""
    <div class='card card-gold'>
    <p>A second Glue Crawler (<code>processed-crawler</code>) auto-created queryable tables in <code>movie_db</code>.
    Athena executed SQL directly on S3 — <b style='color:#E8B84B;'>no data movement required.</b>
    Results were saved as UUID-named CSVs in the Gold layer and loaded directly into Power BI.</p>
    </div>
    """, unsafe_allow_html=True)
    queries = {
        "Genre Performance":"SELECT genre, avg_genre_rating, movie_count\nFROM genre_analytics\nORDER BY avg_genre_rating DESC;",
        "Year Trends":"SELECT year, movies_per_year, avg_rating_by_year\nFROM year_analytics WHERE year BETWEEN 1980 AND 2020\nORDER BY year;",
        "Top Rated Movies":"SELECT title, avg_rating, total_ratings\nFROM enriched_movies WHERE total_ratings > 50\nORDER BY avg_rating DESC LIMIT 10;",
        "Movie Classification":"""SELECT title, avg_rating, total_ratings,
  CASE
    WHEN avg_rating >= 3.8 AND total_ratings < 500 THEN 'Hidden Gem'
    WHEN total_ratings >= 5000                      THEN 'Blockbuster'
    ELSE 'Regular'
  END AS classification
FROM enriched_movies WHERE avg_rating IS NOT NULL;""",
        "Best Per Genre":"""SELECT genre, title, avg_rating,
  ROW_NUMBER() OVER (PARTITION BY genre ORDER BY avg_rating DESC) AS rn
FROM enriched_movies WHERE rn = 1;""",
        "Rating Tiers":"""SELECT
  CASE WHEN avg_rating >= 4.5 THEN 'Masterpiece'
       WHEN avg_rating >= 4.0 THEN 'Great'
       WHEN avg_rating >= 3.5 THEN 'Good'
       WHEN avg_rating >= 3.0 THEN 'Average'
       ELSE 'Below Average' END AS rating_tier,
  COUNT(*) AS movie_count
FROM enriched_movies WHERE avg_rating IS NOT NULL GROUP BY 1;""",
    }
    for name, sql in queries.items():
        with st.expander(f"📄 {name}"):
            st.code(sql, language="sql")
    st.markdown("""
    <div class='card' style='margin-top:16px;'>
    <div style='font-size:0.82rem;color:#8899AA;margin-bottom:10px;'>Each Athena query produces a UUID-named CSV in the Gold bucket, loaded directly into Power BI:</div>
    <div style='font-family:Space Mono,monospace;font-size:0.76rem;color:#E8B84B;line-height:2.2;'>
        s3://anime-gold-aadi-2026/athena-results/<br>
        ├── 214feae7-xxxx.csv &nbsp;← best_per_genre<br>
        ├── 3a8f1bc2-xxxx.csv &nbsp;← genre_scatter<br>
        ├── c7b3a591-xxxx.csv &nbsp;← decade_heatmap<br>
        ├── ... (10 CSV files total)
    </div>
    </div>
    """, unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
elif "Power BI" in page:
    st.markdown("# 📊 Power BI Dashboard")
    st.markdown("""
    <div class='card card-teal'>
    <p>The final dashboard consists of <b style='color:#F0F4F8;'>3 pages</b> in Power BI Desktop,
    themed with a dark navy + gold colour system. All data was loaded from 10 Gold-layer CSVs produced by Athena.</p>
    </div>
    """, unsafe_allow_html=True)

    # ── PAGE 1 ─────────────────────────────────────────────────────────────
    st.markdown("<div class='page-tab pt-1'><span class='pt-num'>Page 1</span><span class='pt-title'>The Big Picture — Overview Dashboard</span></div>", unsafe_allow_html=True)
    show_screenshot("dashboard_page1.png", "Page 1 — Movies Trends Analysis")

    chart_card("KPI Card","ca-kpi","Year Range: 1970–2014",
        "Shows the full temporal scope of the dataset — the analysis covers 44 years of cinema history.",
        "Our dataset spans 44 years of movies, giving us a rich longitudinal view of how cinema evolved.")
    chart_card("KPI Card","ca-kpi","Top Title: Band of Brothers",
        "Highlights the highest-rated title in the entire dataset. This card dynamically updates based on applied filters.",
        "This card always surfaces the top-rated title currently in view — it's reactive to any slicer selection.")
    chart_card("KPI Card","ca-kpi","Total Ratings: 32K",
        "Sum of all user ratings across the dataset — a measure of audience engagement and dataset volume, not an average score.",
        "32,000 total ratings gives us sufficient data density to draw statistically meaningful conclusions.")
    chart_card("KPI Card","ca-kpi","Average Rating: 4.24",
        "Mean rating across all movies. A 4.24 out of 5 confirms the dataset skews toward critically recognised, quality content.",
        "The high average of 4.24 tells us this isn't a random cross-section of cinema — it focuses on recognised films.")
    chart_card("Column Chart","ca-bar","Number of Movies by Year",
        "Column chart showing movie volume per year from 1970–2014. The dashed trend line confirms a clear upward growth pattern with production accelerating post-2000. The sharp drop at 2014 reflects incomplete data for that year.",
        "This chart reveals the democratisation of filmmaking — as technology became accessible, production exploded in the 2000s. The trendline confirms this is structural growth, not a spike.")
    chart_card("Donut Chart","ca-donut","Movies by Rating Tier",
        "Categorises all movies into Masterpiece, Great, Good, Average, and Below Average tiers. The largest segment (28%) is 'Good (3.0–3.5)'. Masterpieces make up only a small fraction — realistic and validates data calibration.",
        "The distribution follows a natural bell-curve — most movies are 'Good', very few are masterpieces. This confirms our rating tiers are well-calibrated against real critical consensus.")
    chart_card("Horizontal Bar","ca-bar","Rating by Movie Title (Top 10 Most Reviewed)",
        "Shows the top 10 movies by total rating count. Pulp Fiction and Forrest Gump lead. High total ratings indicate popularity — not necessarily the best average score.",
        "This chart distinguishes popularity from quality. These films have the most reviews, making their average scores the most statistically reliable in the entire dataset.")

    st.markdown("<hr style='border-color:#243347;margin:28px 0;'>", unsafe_allow_html=True)

    # ── PAGE 2 ─────────────────────────────────────────────────────────────
    st.markdown("<div class='page-tab pt-2'><span class='pt-num'>Page 2</span><span class='pt-title'>Genre Intelligence — Deep Dive by Genre</span></div>", unsafe_allow_html=True)
    show_screenshot("dashboard_page2.png", "Page 2 — Genre Intelligence")

    chart_card("Slicer","ca-slicer","Genre Filter Tiles",
        "Two rows of clickable tile buttons (Action, Animation, Comedy… etc.) that filter all four charts on the page simultaneously — an interactive control that makes the whole page dynamic.",
        "These slicers let us isolate any genre instantly. All four visuals update in sync, enabling real-time genre comparison without navigating away.")
    chart_card("Bubble / Scatter Chart","ca-scatter","Genre Quality vs Popularity Matrix ⭐",
        "The analytically most powerful chart in the dashboard. X-axis = number of movies (volume), Y-axis = average rating (quality), bubble size = popularity score. Four quadrants are labelled. Drama sits top-right as the clear winner — Popular & Great.",
        "This is a strategic decision matrix. Drama is Popular and Great. Film-Noir is Niche but Great. Horror is Popular but Weak. This kind of insight is impossible to see from tables alone — it requires two simultaneous dimensions.")
    chart_card("Grouped Horizontal Bar","ca-bar","Min, Mean & Max Rating by Genre",
        "Three bars per genre showing minimum, mean, and maximum rating. Reveals rating consistency — narrow min-max ranges = more predictable genres. Documentary is most consistent; Horror shows the widest variance.",
        "This chart shows genre reliability. A wide min-max gap means high risk — you might get a masterpiece or a terrible film. Documentary's tight range means it's the safest genre bet for quality.")
    chart_card("Table","ca-table","Best Film per Genre",
        "Single highest-rated film per genre: Action → Band of Brothers, Comedy → Dr. Strangelove, Western → Once Upon a Time in the West, Romance → Casablanca, Horror → Diabolique.",
        "This serves as a recommendation engine — if someone wants to explore a genre, this gives them the definitive critically-validated starting point.")
    chart_card("Heat Map / Matrix","ca-heatmap","Movies per Genre by Decade",
        "Matrix with genres as rows, decades (1960–2010) as columns. Cell colour intensity = movie count (darker red = higher volume). Drama dominates in the 1990s–2000s. Film-Noir effectively disappeared after the 1960s.",
        "The heatmap reveals genre lifecycle trends. Action grew from 77 movies in the 1960s to 676 by 2000. Film-Noir died out after the 1960s. These trends reflect real cultural and industry shifts — not just data patterns.")

    st.markdown("<hr style='border-color:#243347;margin:28px 0;'>", unsafe_allow_html=True)

    # ── PAGE 3 ─────────────────────────────────────────────────────────────
    st.markdown("<div class='page-tab pt-3'><span class='pt-num'>Page 3</span><span class='pt-title'>What to Watch — Recommendations Engine</span></div>", unsafe_allow_html=True)
    show_screenshot("dashboard_page3.png", "Page 3 — What to Watch · Recommendations Engine")

    chart_card("Ranked Table","ca-table","Hidden Gems — Critically Loved, Undiscovered ⭐",
        "Movies with high average ratings but low total review counts. Films critics adore but the general public hasn't widely seen: Come and See (1985, 4.33), Day of Wrath (1943, 4.29), Children of Paradise (1945, 4.22).",
        "Hidden Gems is our most creative analytical feature. We defined a 'gem' as high avg_rating + low total_ratings. This is a quality signal that pure popularity metrics would completely miss — it's our original contribution to the analysis.")
    chart_card("Horizontal Bar","ca-bar","Blockbusters — Popular AND Great",
        "Movies passing both a popularity AND quality threshold simultaneously. Pulp Fiction leads, then Forrest Gump, Star Wars IV, Braveheart, Terminator 2, Schindler's List. X-axis = total ratings count.",
        "These aren't just the most reviewed films — they had to pass a quality filter too. That intersection of mass appeal AND critical quality is rare and genuinely meaningful.")
    chart_card("Horizontal Bar","ca-bar","Best Rated Movie in Each Genre",
        "Top-rated film per genre visualised as a ranked bar chart. All top-genre films score 4.2–4.3. The bars are nearly equal in length across all genres.",
        "The near-uniform bar lengths are an interesting finding — the ceiling of quality is similar across all genres. A great Drama is about as good as a great Western or Sci-Fi. Genre determines average quality, not peak quality.")
    chart_card("Dropdown Slicer","ca-slicer","Genre Filter (Dropdown)",
        "Dropdown slicer filtering both Hidden Gems table and Blockbusters bar chart simultaneously by genre.",
        "This makes Page 3 a personalised recommendation engine. Every genre fan gets a custom view — 'What are the hidden gems in Horror?' or 'Which Sci-Fi blockbusters earned their popularity?'")

    st.markdown("<hr style='border-color:#243347;margin:28px 0;'>", unsafe_allow_html=True)
    st.markdown("### 🎨 Dashboard Theme — Colour System")
    cols = st.columns(6)
    for col_el, (hex_, name) in zip(cols, [
        ("#0F1923","Background"),("#1A2535","Surface"),("#E8B84B","Gold"),
        ("#2E86AB","Teal"),("#3BB273","Green"),("#E84855","Red")
    ]):
        with col_el:
            st.markdown(f"""
            <div style='text-align:center;'>
                <div style='background:{hex_};border:1px solid #243347;border-radius:8px;height:42px;margin-bottom:5px;'></div>
                <div style='font-family:Space Mono,monospace;font-size:0.62rem;color:#E8B84B;'>{hex_}</div>
                <div style='font-size:0.67rem;color:#8899AA;'>{name}</div>
            </div>
            """, unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
elif "Challenges" in page:
    st.markdown("# ⚡ Challenges & How We Solved Them")
    for icon, title, problem, solution, tag in [
        ("⏱️","Glue ETL Timeout on 20M Rows",
         "The initial Visual ETL job processed all 20M ratings rows in a full Spark JOIN with 2 workers. Ran for 26–27 minutes across two attempts before being cancelled — zero output produced.",
         "Applied 10% statistical sampling (seed=42) BEFORE the join, and switched to aggregate-before-join. Reduced intermediate data from 2M to 27K rows. Job completed in 2 minutes 36 seconds.",
         "Performance · Sampling"),
        ("🖱️","Visual ETL Node Misconfiguration",
         "Glue's drag-and-drop Visual ETL created an incorrect JOIN topology — joining full datasets before applying any filters, causing resource exhaustion.",
         "Replaced Visual ETL entirely with a hand-written PySpark script, giving full control over execution order and optimisation.",
         "ETL Design"),
        ("🔢","CREATE EXTERNAL TABLE Syntax Error in Athena",
         "Manual DDL SQL table creation failed — Athena's EXTERNAL TABLE syntax requires precise S3 path matching and SerDe configuration that's error-prone.",
         "Ran a second Glue Crawler on the Silver bucket output. Glue auto-inferred schemas and created correct catalog tables, eliminating manual DDL.",
         "Athena · Crawlers"),
        ("💾","Large Intermediate JOIN Dataset",
         "Naive JOIN of movies.csv (27K rows) × ratings (2M rows) produces a 2M-row intermediate result that must fit in Spark memory before aggregation can reduce it.",
         "Inverted the pipeline: aggregate first (2M → 27K rows), then join the compact result. JOIN intermediate is now just 27K rows — a 10x memory reduction.",
         "Memory Optimisation"),
        ("🖥️","Glue Version Compatibility",
         "Glue version 5.0 with 10 workers caused unexpectedly long bootstrap and initialisation times, making debugging slow and expensive.",
         "Downgraded to Glue 4.0, reduced to 2 G.1X workers. Faster cold-start, lower cost, sufficient compute for sampled dataset.",
         "Infrastructure"),
    ]:
        st.markdown(f"""
        <div style='background:#1E2D40;border:1px solid #243347;border-radius:10px;padding:18px 20px;margin-bottom:12px;'>
        <div style='display:flex;gap:14px;align-items:flex-start;'>
            <div style='font-size:1.5rem;flex-shrink:0;'>{icon}</div>
            <div style='flex:1;'>
                <div style='font-family:Space Mono,monospace;font-size:0.85rem;color:#E84855;margin-bottom:7px;'>{title}</div>
                <div style='font-size:0.82rem;color:#8899AA;line-height:1.6;margin-bottom:8px;'>
                    <b style='color:#F0F4F8;'>Problem: </b>{problem}</div>
                <div style='font-size:0.82rem;color:#8899AA;line-height:1.6;margin-bottom:8px;'>
                    <b style='color:#3BB273;'>Solution: </b>{solution}</div>
                <span style='background:#1A3020;color:#3BB273;border-radius:4px;font-size:0.68rem;padding:2px 8px;'>{tag}</span>
            </div>
        </div>
        </div>
        """, unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
elif "Insights" in page:
    st.markdown("# 💡 Key Analytical Insights")
    st.markdown("""
    <div class='card card-gold'>
    <p>Derived from Athena SQL queries on the Silver layer and visualised across the 3-page Power BI dashboard.
    Based on ~2M ratings (10% stratified sample of the 20M MovieLens dataset).</p>
    </div>
    """, unsafe_allow_html=True)
    for icon, title, desc in [
        ("🎭","Drama dominates volume — Documentary wins on consistency",
         "Drama has the highest movie count and sits top-right on the Quality vs Popularity scatter. But Documentary has the tightest min-max rating range — it's the most consistently rated genre. Volume and consistency are different dimensions of dominance."),
        ("📅","Movie production democratised post-2000",
         "The Number of Movies by Year chart shows flat production through the 1970s–1990s, then steep acceleration post-2000. The dashed trendline confirms structural growth — driven by digital filmmaking, streaming demand, and reduced production costs."),
        ("💎","Hidden gems are systematically missed by popularity metrics",
         "Come and See (1985) and Children of Paradise (1945) score 4.22–4.33 but appear in no popularity rankings. A pure total-ratings sort would never surface them. High avg_rating + low total_ratings is a more meaningful quality signal."),
        ("📊","Pre-aggregation cut Athena compute by ~90%",
         "Computing genre and year aggregations in the ETL layer means Athena scans pre-aggregated tables of ~20 rows instead of enriched_movies with 27K rows per query. This is a core data lakehouse design principle — push computation upstream."),
        ("🎬","Quality ceiling is uniform across genres",
         "The Best Rated Movie in Each Genre bar chart shows near-identical bar lengths (4.2–4.3) across all genres. The ceiling of excellence is genre-agnostic — a great Western is as good as a great Sci-Fi film."),
        ("⚙️","10% sampling preserved statistical integrity",
         "The fixed-seed 10% sample retained ~120K of 138K users and ~25K of 27K movies. By the law of large numbers, aggregated metrics are statistically indistinguishable from the full 20M dataset."),
    ]:
        st.markdown(f"""
        <div class='challenge'><div class='icon'>{icon}</div>
        <div><div class='ctitle' style='color:#E8B84B!important;'>{title}</div>
        <div class='sol'>{desc}</div></div></div>
        """, unsafe_allow_html=True)
    st.markdown("### Technologies Mastered")
    cols = st.columns(4)
    for i, (icon, name, role) in enumerate([
        ("🪣","Amazon S3","Data Lake Design"),("⚙️","AWS Glue","Crawler + ETL"),
        ("🔍","Amazon Athena","Serverless SQL"),("📊","Power BI","3-Page Dashboard"),
        ("🐍","PySpark","Distributed ETL"),("🔐","AWS IAM","Role Management"),
        ("📋","SQL","Query Layer"),("🎨","DAX","BI Measures"),
    ]):
        with cols[i % 4]:
            st.markdown(f"""
            <div class='tech-item' style='margin-bottom:10px;'>
                <div class='t-icon'>{icon}</div>
                <div class='t-name'>{name}</div>
                <div class='t-role'>{role}</div>
            </div>
            """, unsafe_allow_html=True)
