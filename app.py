import streamlit as st

st.set_page_config(
    page_title="MovieLens DEA Pipeline",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ─── Custom CSS ───────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=DM+Sans:wght@300;400;500;600&display=swap');

:root {
    --bg:       #0F1923;
    --surface:  #1A2535;
    --surface2: #1E2D40;
    --gold:     #E8B84B;
    --teal:     #2E86AB;
    --green:    #3BB273;
    --red:      #E84855;
    --text:     #F0F4F8;
    --muted:    #8899AA;
    --border:   #243347;
}

html, body, [data-testid="stAppViewContainer"] {
    background-color: var(--bg) !important;
    color: var(--text) !important;
    font-family: 'DM Sans', sans-serif;
}

[data-testid="stSidebar"] {
    background-color: var(--surface) !important;
    border-right: 1px solid var(--border);
}

[data-testid="stSidebar"] * { color: var(--text) !important; }

h1,h2,h3,h4 { font-family: 'Space Mono', monospace !important; color: var(--gold) !important; }

.stMarkdown p { color: var(--text); line-height: 1.7; }

/* Cards */
.card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 24px;
    margin-bottom: 16px;
}
.card-gold  { border-left: 4px solid var(--gold);  }
.card-teal  { border-left: 4px solid var(--teal);  }
.card-green { border-left: 4px solid var(--green); }
.card-red   { border-left: 4px solid var(--red);   }

/* KPI boxes */
.kpi-row { display: flex; gap: 16px; flex-wrap: wrap; margin: 20px 0; }
.kpi {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 20px 28px;
    flex: 1; min-width: 160px; text-align: center;
}
.kpi .num { font-family: 'Space Mono', monospace; font-size: 2rem; color: var(--gold); }
.kpi .lbl { font-size: 0.78rem; color: var(--muted); margin-top: 4px; text-transform: uppercase; letter-spacing: 1px; }

/* Pipeline flow */
.pipeline {
    display: flex; align-items: center; gap: 0;
    overflow-x: auto; padding: 24px 0; margin: 20px 0;
}
.pipe-step {
    background: var(--surface2);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 16px 20px;
    text-align: center;
    min-width: 120px;
}
.pipe-step .icon { font-size: 1.8rem; }
.pipe-step .name { font-family: 'Space Mono', monospace; font-size: 0.7rem; color: var(--gold); margin-top: 6px; }
.pipe-step .sub  { font-size: 0.65rem; color: var(--muted); margin-top: 3px; }
.pipe-arrow { color: var(--gold); font-size: 1.5rem; padding: 0 8px; flex-shrink: 0; }

/* Layer badges */
.badge {
    display: inline-block;
    padding: 3px 12px;
    border-radius: 20px;
    font-size: 0.72rem;
    font-family: 'Space Mono', monospace;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-right: 6px;
}
.badge-bronze { background: #3D2B1A; color: #CD7F32; border: 1px solid #CD7F32; }
.badge-silver { background: #1E2535; color: #C0C0C0; border: 1px solid #C0C0C0; }
.badge-gold   { background: #2A2210; color: var(--gold); border: 1px solid var(--gold); }

/* Stage boxes */
.stage {
    background: var(--surface2);
    border-radius: 10px;
    padding: 18px 22px;
    margin-bottom: 12px;
    border: 1px solid var(--border);
    position: relative;
}
.stage-num {
    position: absolute; top: -10px; left: 16px;
    background: var(--gold); color: var(--bg);
    font-family: 'Space Mono', monospace;
    font-size: 0.7rem; font-weight: 700;
    padding: 2px 10px; border-radius: 20px;
}
.stage h4 { color: var(--text) !important; font-size: 0.95rem !important; margin: 8px 0 6px 0; }
.stage p, .stage li { font-size: 0.88rem; color: var(--muted); line-height: 1.6; }

/* Code block override */
.stCode { background: #0A1018 !important; border: 1px solid var(--border) !important; }

/* Challenge row */
.challenge {
    display: flex; gap: 16px;
    background: var(--surface2);
    border-radius: 10px;
    padding: 16px 20px;
    margin-bottom: 10px;
    border: 1px solid var(--border);
    align-items: flex-start;
}
.challenge .icon { font-size: 1.4rem; flex-shrink: 0; margin-top: 2px; }
.challenge .title { font-family: 'Space Mono', monospace; font-size: 0.82rem; color: var(--red); }
.challenge .sol   { font-size: 0.84rem; color: var(--text); margin-top: 4px; }
.challenge .tag   { display:inline-block; background: #1A3020; color: var(--green); border-radius: 4px; font-size: 0.7rem; padding: 2px 8px; margin-top: 6px; }

/* Tech card */
.tech-grid { display: flex; flex-wrap: wrap; gap: 12px; margin: 16px 0; }
.tech-item {
    background: var(--surface2);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 12px 16px;
    min-width: 140px; flex: 1;
    text-align: center;
}
.tech-item .t-icon { font-size: 1.6rem; }
.tech-item .t-name { font-family: 'Space Mono', monospace; font-size: 0.72rem; color: var(--gold); margin-top: 6px; }
.tech-item .t-role { font-size: 0.68rem; color: var(--muted); margin-top: 3px; }

/* Header */
.hero {
    background: linear-gradient(135deg, #1A2535 0%, #0F1923 60%);
    border: 1px solid var(--border);
    border-radius: 16px;
    padding: 40px 48px;
    margin-bottom: 28px;
    position: relative;
    overflow: hidden;
}
.hero::before {
    content: '';
    position: absolute; top: 0; right: 0;
    width: 300px; height: 100%;
    background: radial-gradient(circle at 80% 50%, rgba(232,184,75,0.06) 0%, transparent 70%);
}
.hero h1 { font-size: 2rem !important; margin: 0 0 8px 0 !important; }
.hero .sub { color: var(--muted); font-size: 1rem; }
.hero .authors { margin-top: 20px; display: flex; gap: 20px; flex-wrap: wrap; }
.author-chip {
    background: var(--surface2);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 8px 16px;
    font-size: 0.82rem;
}
.author-chip span { color: var(--gold); font-family: 'Space Mono', monospace; }

/* Section divider */
.divider { border: none; border-top: 1px solid var(--border); margin: 28px 0; }

/* Streamlit tab overrides */
[data-baseweb="tab-list"] { background: var(--surface) !important; border-radius: 8px; }
[data-baseweb="tab"] { color: var(--muted) !important; }
[aria-selected="true"] { color: var(--gold) !important; border-bottom-color: var(--gold) !important; }

[data-testid="metric-container"] { background: var(--surface) !important; border: 1px solid var(--border) !important; border-radius: 10px !important; padding: 16px !important; }

/* Expander */
[data-testid="stExpander"] { background: var(--surface2) !important; border: 1px solid var(--border) !important; border-radius: 8px !important; }

/* Scrollbar */
::-webkit-scrollbar { width: 6px; height: 6px; }
::-webkit-scrollbar-track { background: var(--bg); }
::-webkit-scrollbar-thumb { background: var(--border); border-radius: 3px; }
</style>
""", unsafe_allow_html=True)

# ─── Sidebar ──────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style='padding: 8px 0 20px 0;'>
        <div style='font-family: Space Mono, monospace; font-size:1.1rem; color:#E8B84B;'>🎬 MovieLens DEA</div>
        <div style='font-size:0.72rem; color:#8899AA; margin-top:4px;'>Data Engineering & Analytics Pipeline</div>
    </div>
    """, unsafe_allow_html=True)

    page = st.radio("Navigate", [
        "🏠  Overview",
        "🏗️  Architecture",
        "⚙️  Preprocessing",
        "🔄  Transformation",
        "🗄️  Athena & Gold Layer",
        "📊  Power BI Dashboard",
        "⚡  Challenges & Solutions",
        "💡  Key Insights",
    ], label_visibility="collapsed")

    st.markdown("<hr style='border-color:#243347; margin: 20px 0;'>", unsafe_allow_html=True)
    st.markdown("""
    <div style='font-size:0.72rem; color:#8899AA;'>
        <div style='margin-bottom:6px;'><span style='color:#E8B84B;'>▸</span> Parth Bisht · 23/IT/117</div>
        <div><span style='color:#E8B84B;'>▸</span> Ishaan Yadav · 23/IT/73</div>
    </div>
    """, unsafe_allow_html=True)

# ─── PAGE: Overview ───────────────────────────────────────────────────────────
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
        <div class='kpi'><div class='num'>4</div><div class='lbl'>BI Dashboard Pages</div></div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### Project Overview")
    st.markdown("""
    <div class='card card-teal'>
    <p>This project demonstrates an <b style='color:#F0F4F8;'>end-to-end cloud-based Data Engineering and Analytics (DEA) pipeline</b>
    built entirely on Amazon Web Services. The pipeline ingests a large-scale real-world movies dataset,
    transforms and enriches it using distributed PySpark computing, and delivers analytical insights through
    an interactive Power BI dashboard.</p>
    <p>The architecture follows an industry-standard <b style='color:#E8B84B;'>Bronze → Silver → Gold lakehouse pattern</b>,
    ensuring data quality, traceability, and clean separation of concerns across every stage.</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("#### 📦 Dataset")
        st.markdown("""
        <div class='card'>
        <div><span class='badge badge-gold'>Source</span> MovieLens 20M · GroupLens Research, UMN</div>
        <div style='margin-top:12px; font-size:0.85rem; color:#8899AA;'>
            <div style='margin-bottom:6px;'>📄 <b style='color:#F0F4F8;'>movies.csv</b> — movieId, title, genres</div>
            <div style='margin-bottom:6px;'>⭐ <b style='color:#F0F4F8;'>ratings.csv</b> — userId, movieId, rating, timestamp (20M rows)</div>
            <div>🏷️ <b style='color:#F0F4F8;'>tags.csv</b> — userId, movieId, tag, timestamp</div>
        </div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("#### 🛠️ Stack")
        st.markdown("""
        <div class='tech-grid'>
            <div class='tech-item'><div class='t-icon'>🪣</div><div class='t-name'>Amazon S3</div><div class='t-role'>Data Lake</div></div>
            <div class='tech-item'><div class='t-icon'>⚙️</div><div class='t-name'>AWS Glue</div><div class='t-role'>ETL · PySpark</div></div>
            <div class='tech-item'><div class='t-icon'>🔍</div><div class='t-name'>Athena</div><div class='t-role'>SQL Query Layer</div></div>
            <div class='tech-item'><div class='t-icon'>📊</div><div class='t-name'>Power BI</div><div class='t-role'>Visualisation</div></div>
        </div>
        """, unsafe_allow_html=True)

# ─── PAGE: Architecture ───────────────────────────────────────────────────────
elif "Architecture" in page:
    st.markdown("# 🏗️ AWS Architecture")
    st.markdown("### Full Pipeline Flow")

    st.markdown("""
    <div class='pipeline'>
        <div class='pipe-step'>
            <div class='icon'>📄</div>
            <div class='name'>RAW CSVs</div>
            <div class='sub'>Kaggle · MovieLens</div>
        </div>
        <div class='pipe-arrow'>→</div>
        <div class='pipe-step' style='border-color:#CD7F32;'>
            <div class='icon'>🪣</div>
            <div class='name'>BRONZE</div>
            <div class='sub'>S3 · Immutable</div>
        </div>
        <div class='pipe-arrow'>→</div>
        <div class='pipe-step'>
            <div class='icon'>🕷️</div>
            <div class='name'>GLUE CRAWLER</div>
            <div class='sub'>Schema Discovery</div>
        </div>
        <div class='pipe-arrow'>→</div>
        <div class='pipe-step'>
            <div class='icon'>⚙️</div>
            <div class='name'>GLUE ETL</div>
            <div class='sub'>PySpark Transform</div>
        </div>
        <div class='pipe-arrow'>→</div>
        <div class='pipe-step' style='border-color:#C0C0C0;'>
            <div class='icon'>🪣</div>
            <div class='name'>SILVER</div>
            <div class='sub'>S3 · Processed</div>
        </div>
        <div class='pipe-arrow'>→</div>
        <div class='pipe-step'>
            <div class='icon'>🔍</div>
            <div class='name'>ATHENA SQL</div>
            <div class='sub'>Serverless Query</div>
        </div>
        <div class='pipe-arrow'>→</div>
        <div class='pipe-step' style='border-color:#E8B84B;'>
            <div class='icon'>🪣</div>
            <div class='name'>GOLD</div>
            <div class='sub'>S3 · Analytics CSVs</div>
        </div>
        <div class='pipe-arrow'>→</div>
        <div class='pipe-step'>
            <div class='icon'>📊</div>
            <div class='name'>POWER BI</div>
            <div class='sub'>Dashboard</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### Data Lake Layers")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class='card' style='border-top:3px solid #CD7F32;'>
            <div><span class='badge badge-bronze'>BRONZE</span></div>
            <div style='font-family:Space Mono,monospace; font-size:0.8rem; color:#F0F4F8; margin:12px 0 6px 0;'>anime-bronze-aadi-2026</div>
            <div style='font-size:0.82rem; color:#8899AA; line-height:1.8;'>
                Raw Zone — <b style='color:#F0F4F8;'>Immutable source of truth.</b><br>
                No transformations applied here ever.<br><br>
                <code style='background:#0A1018; padding:2px 6px; border-radius:4px; font-size:0.75rem;'>raw/movies/movies.csv</code><br>
                <code style='background:#0A1018; padding:2px 6px; border-radius:4px; font-size:0.75rem;'>raw/ratings/ratings.csv</code><br>
                <code style='background:#0A1018; padding:2px 6px; border-radius:4px; font-size:0.75rem;'>raw/tags/tags.csv</code>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class='card' style='border-top:3px solid #C0C0C0;'>
            <div><span class='badge badge-silver'>SILVER</span></div>
            <div style='font-family:Space Mono,monospace; font-size:0.8rem; color:#F0F4F8; margin:12px 0 6px 0;'>anime-silver-aadi-2026</div>
            <div style='font-size:0.82rem; color:#8899AA; line-height:1.8;'>
                Processed Zone — Output of Glue ETL.<br>
                Cleaned, joined, feature-engineered.<br><br>
                <code style='background:#0A1018; padding:2px 6px; border-radius:4px; font-size:0.75rem;'>enriched_movies/</code><br>
                <code style='background:#0A1018; padding:2px 6px; border-radius:4px; font-size:0.75rem;'>genre_analytics/</code><br>
                <code style='background:#0A1018; padding:2px 6px; border-radius:4px; font-size:0.75rem;'>year_analytics/</code>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class='card' style='border-top:3px solid #E8B84B;'>
            <div><span class='badge badge-gold'>GOLD</span></div>
            <div style='font-family:Space Mono,monospace; font-size:0.8rem; color:#F0F4F8; margin:12px 0 6px 0;'>anime-gold-aadi-2026</div>
            <div style='font-size:0.82rem; color:#8899AA; line-height:1.8;'>
                Analytics Zone — Athena query results.<br>
                Dashboard-ready CSVs for Power BI.<br><br>
                <code style='background:#0A1018; padding:2px 6px; border-radius:4px; font-size:0.75rem;'>athena-results/</code><br>
                <code style='background:#0A1018; padding:2px 6px; border-radius:4px; font-size:0.75rem;'>214feae7-....csv</code><br>
                <code style='background:#0A1018; padding:2px 6px; border-radius:4px; font-size:0.75rem;'>(UUID-named by Athena)</code>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("### AWS Services Used")
    services = [
        ("🪣", "Amazon S3", "Three-zone data lake: Bronze (raw), Silver (processed), Gold (analytics results)"),
        ("🕷️", "Glue Crawler", "Auto-infers schema from raw CSVs, creates tables in Glue Data Catalog"),
        ("⚙️", "Glue ETL Job", "PySpark-based transformation — sampling, join, aggregation, feature engineering"),
        ("📚", "Glue Data Catalog", "Metadata store — holds table definitions for movie_db and processed tables"),
        ("🔍", "Amazon Athena", "Serverless SQL engine to query processed S3 data and produce Gold layer CSVs"),
        ("🔐", "AWS IAM", "GlueS3Role-Aadi — grants Glue full S3 and Glue service permissions"),
    ]
    for icon, name, desc in services:
        st.markdown(f"""
        <div class='challenge'>
            <div class='icon'>{icon}</div>
            <div><div class='title'>{name}</div><div class='sol'>{desc}</div></div>
        </div>
        """, unsafe_allow_html=True)

# ─── PAGE: Preprocessing ─────────────────────────────────────────────────────
elif "Preprocessing" in page:
    st.markdown("# ⚙️ Data Preprocessing Pipeline")
    st.markdown("""
    <div class='card card-gold'>
    <p>The Glue ETL job executed a <b style='color:#E8B84B;'>5-stage preprocessing pipeline in PySpark</b>,
    reading directly from Bronze S3 paths and writing structured CSVs to the Silver layer.
    Each stage had a deliberate purpose — this was not a monolithic script but a structured data engineering workflow.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### The 5-Stage Pipeline")

    stages = [
        ("Stage 1", "🧹 Cleaning", [
            "<b>Type casting:</b> movieId cast to INT, rating cast to DOUBLE from raw string format",
            "<b>Null strategy:</b> LEFT JOIN used to retain movies with no associated ratings — avg_rating stored as NULL, preserving dataset completeness rather than silently dropping unrated movies",
            "<b>Philosophy:</b> Never destroy data at the source — the Bronze layer remains fully intact; cleaning only produces a new, better Silver copy",
        ], "teal"),
        ("Stage 2", "✂️ Pruning / Sampling", [
            "<b>Problem:</b> ratings.csv had 20 million rows — unprocessable with 2 Glue workers in full",
            "<b>Solution:</b> 10% random sample applied to ratings BEFORE any JOIN operation",
            "<code>df_ratings_sample = df_ratings.sample(fraction=0.1, seed=42)</code>",
            "<b>Statistical validity:</b> ~2M rows retained · ~120K of 138K users · ~25K of 27K movies — law of large numbers ensures aggregated metrics are statistically indistinguishable from full data",
            "<b>Seed=42:</b> fixed seed guarantees full reproducibility across pipeline re-runs",
        ], "red"),
        ("Stage 3", "🔄 Transformation (Join)", [
            "Aggregation computed on ratings <b>BEFORE</b> the join — this is the key optimisation",
            "Per-movie avg_rating and total_ratings computed first, reducing 2M rows → 27K movie-level rows",
            "movies.csv then LEFT JOINed against this compact 27K-row result on movieId",
            "<code>df_ratings_agg = df_ratings_sample.groupBy('movieId').agg(avg('rating'), count('rating'))</code>",
            "tags.csv was ingested to Bronze layer for future use but excluded from core ETL join",
        ], "teal"),
        ("Stage 4", "🔧 Feature Engineering", [
            "<b>Year extraction:</b> regex applied to title field → extracts 4-digit year from brackets",
            "Example: <code>'Toy Story (1995)'</code> → <code>year = 1995</code> stored as INT",
            "<b>Genre explosion:</b> pipe-delimited genre strings split into individual rows",
            "Example: <code>'Adventure|Children|Fantasy'</code> → 3 separate rows per movie",
            "This enables genre-level GROUP BY aggregations downstream in Athena",
        ], "gold"),
        ("Stage 5", "📦 Aggregation & Output", [
            "<b>Genre-level:</b> GROUP BY genre → avg_genre_rating, movie_count → saved to genre_analytics/",
            "<b>Year-level:</b> GROUP BY year → movies_per_year, avg_rating_by_year → saved to year_analytics/",
            "Pre-aggregating at ETL time significantly reduces Athena query compute costs and response times",
            "Three CSV datasets written to Silver layer with Spark's distributed write",
        ], "green"),
    ]

    for num, title, bullets, color in stages:
        with st.expander(f"{title} — {title.split(' ')[1]}", expanded=True):
            html = f"""
            <div class='stage'>
                <div class='stage-num'>{num}</div>
                <h4>{title}</h4>
                <ul style='margin:0; padding-left:18px;'>
            """
            for b in bullets:
                html += f"<li style='margin-bottom:6px; color:#8899AA; font-size:0.87rem;'>{b}</li>"
            html += "</ul></div>"
            st.markdown(html, unsafe_allow_html=True)

    st.markdown("### Transformation Summary Table")
    import pandas as pd
    df = pd.DataFrame([
        ("Type Casting", "movieId → INT, rating → DOUBLE from raw strings"),
        ("Statistical Sampling", "10% random sample (seed=42): 20M rows → ~2M rows retained"),
        ("Aggregation before Join", "Per-movie avg_rating + total_ratings computed before join — reduces join size by 10x"),
        ("Relational Join", "movies.csv LEFT JOIN aggregated ratings on movieId"),
        ("Year Extraction", "Regex on title field: 'Toy Story (1995)' → year = 1995"),
        ("Genre Explosion", "'Adventure|Children|Fantasy' → 3 individual genre rows per movie"),
        ("Null Handling", "Left join preserves movies with no ratings (NULL avg_rating retained)"),
        ("Pre-Aggregation", "Genre-level and year-level GROUP BY computed at ETL time for query efficiency"),
    ], columns=["Transformation Stage", "What Was Done"])
    st.dataframe(df, use_container_width=True, hide_index=True)

    st.markdown("### PySpark Code — Core ETL Logic")
    st.code("""
# ── Stage 2: Pruning ──────────────────────────────────────────────────────────
df_ratings = spark.read.csv("s3://anime-bronze-aadi-2026/raw/ratings/", header=True)
df_ratings_sample = df_ratings.sample(fraction=0.1, seed=42)  # 20M → ~2M rows

# ── Stage 3: Aggregate BEFORE join (key optimisation) ────────────────────────
from pyspark.sql.functions import avg, count, col, regexp_extract, explode, split

df_agg = df_ratings_sample.groupBy("movieId").agg(
    avg("rating").alias("avg_rating"),
    count("rating").alias("total_ratings")
)
# Result: ~27,000 rows (one per movie) — massively smaller than 2M

# ── Stage 3: Join ─────────────────────────────────────────────────────────────
df_movies = spark.read.csv("s3://anime-bronze-aadi-2026/raw/movies/", header=True)
df_enriched = df_movies.join(df_agg, on="movieId", how="left")

# ── Stage 4: Feature Engineering ─────────────────────────────────────────────
df_enriched = df_enriched.withColumn(
    "year", regexp_extract(col("title"), r"\\((\\d{4})\\)", 1).cast("int")
)
df_exploded = df_enriched.withColumn(
    "genre", explode(split(col("genres"), "\\\\|"))
)

# ── Stage 5: Pre-Aggregation & Write ─────────────────────────────────────────
genre_agg = df_exploded.groupBy("genre").agg(
    avg("avg_rating").alias("avg_genre_rating"),
    count("movieId").alias("movie_count")
)
genre_agg.write.csv("s3://anime-silver-aadi-2026/movie-analytics/genre_analytics/", header=True)

year_agg = df_enriched.groupBy("year").agg(
    count("movieId").alias("movies_per_year"),
    avg("avg_rating").alias("avg_rating_by_year")
)
year_agg.write.csv("s3://anime-silver-aadi-2026/movie-analytics/year_analytics/", header=True)
df_enriched.write.csv("s3://anime-silver-aadi-2026/movie-analytics/enriched_movies/", header=True)
    """, language="python")

# ─── PAGE: Transformation ────────────────────────────────────────────────────
elif "Transformation" in page:
    st.markdown("# 🔄 Data Transformation — Structure & Schema")

    st.markdown("### Schema Evolution Across Layers")
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class='card' style='border-top:3px solid #CD7F32;'>
            <div><span class='badge badge-bronze'>BRONZE SCHEMA</span> <span style='font-size:0.75rem; color:#8899AA;'>Raw — unmodified</span></div>
            <div style='margin-top:14px;'>
        """, unsafe_allow_html=True)
        st.code("""movies.csv
─────────────────────────────
movieId   STRING  (raw)
title     STRING  (e.g. "Toy Story (1995)")
genres    STRING  (e.g. "Adventure|Animation")

ratings.csv
─────────────────────────────
userId    STRING
movieId   STRING
rating    STRING  (raw, needs cast)
timestamp STRING
""", language="text")
        st.markdown("</div></div>", unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class='card' style='border-top:3px solid #C0C0C0;'>
            <div><span class='badge badge-silver'>SILVER SCHEMA</span> <span style='font-size:0.75rem; color:#8899AA;'>enriched_movies</span></div>
            <div style='margin-top:14px;'>
        """, unsafe_allow_html=True)
        st.code("""enriched_movies/
─────────────────────────────
movieId       INT      ← cast
title         STRING
genres        STRING   (original)
genre         STRING   ← EXPLODED (one row per genre)
avg_rating    DOUBLE   ← DERIVED from join
total_ratings BIGINT   ← DERIVED from join
year          INT      ← EXTRACTED via regex

genre_analytics/
─────────────────────────────
genre             STRING
avg_genre_rating  DOUBLE
movie_count       BIGINT

year_analytics/
─────────────────────────────
year              INT
movies_per_year   BIGINT
avg_rating_by_year DOUBLE
""", language="text")
        st.markdown("</div></div>", unsafe_allow_html=True)

    st.markdown("### Key Transformation Decisions")

    decisions = [
        ("Aggregate Before Join", "🎯",
         "Standard ETL would join first (20M × 27K rows), then aggregate. We reversed this: aggregate ratings to 27K rows FIRST, then join. This is a 10x reduction in intermediate data size — the single most impactful optimisation in the pipeline.",
         "Performance Optimisation"),
        ("LEFT JOIN over INNER JOIN", "🔗",
         "An INNER JOIN would silently drop movies with zero ratings — distorting genre counts, year distributions, and catalog completeness. The LEFT JOIN preserves all 27K movies while marking unrated ones with NULL avg_rating. This is the correct data engineering choice.",
         "Data Integrity"),
        ("Genre Explosion (1→N rows)", "💥",
         "A movie like 'Adventure|Children|Fantasy' stored as one row cannot be aggregated by genre. Exploding it into 3 rows enables GROUP BY genre queries. This is a deliberate schema denormalisation for analytical purposes — the enriched_movies table is an analytics-first schema, not a transactional one.",
         "Analytical Design"),
        ("Year as Extracted Column", "📅",
         "MovieLens encodes year inside the title string. Storing year as a separate INT column (vs. extracting it at query time with regex) means every downstream query gets a fast, indexed integer filter instead of a slow string pattern match.",
         "Query Performance"),
    ]

    for title, icon, desc, tag in decisions:
        st.markdown(f"""
        <div class='challenge'>
            <div class='icon'>{icon}</div>
            <div>
                <div class='title'>{title}</div>
                <div class='sol'>{desc}</div>
                <span class='tag'>{tag}</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("### Output Tables Written to Silver")
    import pandas as pd
    df = pd.DataFrame([
        ("enriched_movies", "movie-analytics/enriched_movies/", "movieId, title, genres, genre, avg_rating, total_ratings, year", "~27K rows"),
        ("genre_analytics", "movie-analytics/genre_analytics/", "genre, avg_genre_rating, movie_count", "~20 rows"),
        ("year_analytics",  "movie-analytics/year_analytics/",  "year, movies_per_year, avg_rating_by_year", "~50 rows"),
    ], columns=["Table", "S3 Path (Silver)", "Fields", "Approx Rows"])
    st.dataframe(df, use_container_width=True, hide_index=True)

# ─── PAGE: Athena & Gold ──────────────────────────────────────────────────────
elif "Athena" in page:
    st.markdown("# 🗄️ Athena Query Layer — Silver → Gold")

    st.markdown("""
    <div class='card card-gold'>
    <p>A second Glue Crawler (<code>processed-crawler</code>) was run on the Silver bucket output,
    auto-creating queryable tables in <code>movie_db</code>.
    Athena then executed SQL queries directly on S3 data — <b style='color:#E8B84B;'>no data movement required.</b>
    Results were saved as CSV files in the Gold layer and loaded directly into Power BI.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### Athena SQL Queries Run")

    queries = {
        "Genre Performance": """SELECT genre, avg_genre_rating, movie_count
FROM genre_analytics
ORDER BY avg_genre_rating DESC;""",
        "Year Trends": """SELECT year, movies_per_year, avg_rating_by_year
FROM year_analytics
WHERE year BETWEEN 1980 AND 2020
ORDER BY year;""",
        "Top Rated Movies": """SELECT title, avg_rating, total_ratings
FROM enriched_movies
WHERE total_ratings > 50
ORDER BY avg_rating DESC
LIMIT 10;""",
        "Movie Classification (Hidden Gems / Blockbusters)": """SELECT title, avg_rating, total_ratings,
  CASE
    WHEN avg_rating >= 3.8 AND total_ratings < 500  THEN 'Hidden Gem'
    WHEN total_ratings >= 5000                       THEN 'Blockbuster'
    ELSE 'Regular'
  END AS classification
FROM enriched_movies
WHERE avg_rating IS NOT NULL;""",
        "Best Per Genre": """SELECT genre, title, avg_rating, total_ratings,
       ROW_NUMBER() OVER (PARTITION BY genre ORDER BY avg_rating DESC) AS rn
FROM enriched_movies
WHERE rn = 1;""",
        "Rating Tiers": """SELECT
  CASE
    WHEN avg_rating >= 4.5 THEN 'Masterpiece'
    WHEN avg_rating >= 4.0 THEN 'Great'
    WHEN avg_rating >= 3.5 THEN 'Good'
    WHEN avg_rating >= 3.0 THEN 'Average'
    ELSE                        'Below Average'
  END AS rating_tier,
  COUNT(*) AS movie_count
FROM enriched_movies
WHERE avg_rating IS NOT NULL
GROUP BY 1;""",
    }

    for name, sql in queries.items():
        with st.expander(f"📄 {name}"):
            st.code(sql, language="sql")

    st.markdown("### Gold Layer Output Files")
    st.markdown("""
    <div class='card'>
    <p style='color:#8899AA; font-size:0.85rem;'>Each Athena query produces a UUID-named CSV in the Gold bucket. These are loaded directly into Power BI as the final data source.</p>
    <div style='font-family: Space Mono, monospace; font-size:0.78rem; color:#E8B84B; line-height:2; margin-top:12px;'>
        s3://anime-gold-aadi-2026/athena-results/<br>
        ├── 214feae7-xxxx-xxxx-xxxx-xxxxxxxxxxxx.csv  ← best_per_genre<br>
        ├── 3a8f1bc2-xxxx-xxxx-xxxx-xxxxxxxxxxxx.csv  ← best_per_year<br>
        ├── 9d2e4f71-xxxx-xxxx-xxxx-xxxxxxxxxxxx.csv  ← genre_scatter<br>
        ├── c7b3a591-xxxx-xxxx-xxxx-xxxxxxxxxxxx.csv  ← decade_heatmap<br>
        ├── ... (10 CSV files total, one per Power BI table)<br>
    </div>
    </div>
    """, unsafe_allow_html=True)

# ─── PAGE: Power BI ───────────────────────────────────────────────────────────
elif "Power BI" in page:
    st.markdown("# 📊 Power BI Dashboard")

    pages = [
        ("The Big Picture", "Overview KPIs, quality tier donut, top reviewed movies, movies per decade"),
        ("Genre Intelligence", "Scatter: quality vs popularity, genre range bar, decade heatmap, best per genre table"),
        ("Era & Trends", "Dual-axis year chart, best movie per year scrollable table, rating trend with forecast"),
        ("What to Watch", "Hidden gems table, blockbusters bar, best per genre ranked bar, genre filter slicer"),
    ]

    for i, (name, desc) in enumerate(pages, 1):
        st.markdown(f"""
        <div class='card card-teal' style='margin-bottom:12px;'>
            <div style='display:flex; justify-content:space-between; align-items:center;'>
                <div>
                    <span style='font-family:Space Mono,monospace; font-size:0.72rem; color:#8899AA;'>PAGE {i}</span>
                    <div style='font-family:Space Mono,monospace; font-size:1rem; color:#E8B84B; margin-top:2px;'>{name}</div>
                    <div style='font-size:0.84rem; color:#8899AA; margin-top:6px;'>{desc}</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("### Theme & Colour System")
    colours = [
        ("#0F1923", "Background", "bg"),
        ("#1A2535", "Surface", "surface"),
        ("#E8B84B", "Gold — Accent", "gold"),
        ("#2E86AB", "Teal — Primary", "teal"),
        ("#3BB273", "Green — Positive", "green"),
        ("#E84855", "Red — Negative", "red"),
    ]
    cols = st.columns(6)
    for col_el, (hex_, name, _) in zip(cols, colours):
        with col_el:
            st.markdown(f"""
            <div style='text-align:center;'>
                <div style='background:{hex_}; border:1px solid #243347; border-radius:8px; height:48px; margin-bottom:6px;'></div>
                <div style='font-family:Space Mono,monospace; font-size:0.65rem; color:#E8B84B;'>{hex_}</div>
                <div style='font-size:0.7rem; color:#8899AA;'>{name}</div>
            </div>
            """, unsafe_allow_html=True)

# ─── PAGE: Challenges ─────────────────────────────────────────────────────────
elif "Challenges" in page:
    st.markdown("# ⚡ Challenges & How We Solved Them")

    challenges = [
        ("⏱️", "Glue ETL Timeout on 20M Rows",
         "The initial Visual ETL job processed all 20M ratings rows in a full Spark JOIN with only 2 workers. The job ran for 26–27 minutes across two attempts before being manually cancelled, producing zero output.",
         "Applied 10% statistical sampling (seed=42) BEFORE the join. Switched to aggregate-before-join strategy — reduced intermediate data from 2M to 27K rows. Job then completed in 2 minutes 36 seconds.",
         "Performance · Sampling"),
        ("🖱️", "Visual ETL Node Misconfiguration",
         "AWS Glue's Visual ETL drag-and-drop interface created an incorrect JOIN topology — it joined the full datasets before applying any filters or aggregations, causing the resource exhaustion.",
         "Replaced the Visual ETL entirely with a hand-written PySpark script, giving full control over execution order, sampling, and optimisation.",
         "ETL Design"),
        ("🔢", "CREATE EXTERNAL TABLE Syntax Error in Athena",
         "Initial attempt to manually define Athena tables using DDL SQL failed — Athena's EXTERNAL TABLE syntax requires precise S3 path matching and SerDe configuration that's easy to misconfigure.",
         "Ran a second Glue Crawler (processed-crawler) directly on the Silver bucket output. Glue auto-inferred schemas and created correct catalog tables, eliminating manual DDL entirely.",
         "Athena · Crawlers"),
        ("💾", "Large Intermediate JOIN Dataset",
         "A naive JOIN of movies.csv (27K rows) × ratings (2M rows) produces a 2M-row intermediate result that must fit in Spark memory before aggregation can reduce it.",
         "Inverted the pipeline: aggregate first (2M → 27K), then join the compact result. The JOIN intermediate result is now just 27K rows — a 10x memory reduction.",
         "Memory Optimisation"),
        ("📉", "Glue Version Compatibility",
         "Initial test with Glue version 5.0 and 10 workers caused unexpectedly long bootstrap and initialisation times, making debugging slow and expensive.",
         "Downgraded to Glue 4.0, reduced to 2 G.1X workers. Faster cold-start time, lower cost, and sufficient compute for the sampled dataset size.",
         "Infrastructure"),
    ]

    for icon, title, problem, solution, tag in challenges:
        st.markdown(f"""
        <div style='background:var(--surface2, #1E2D40); border:1px solid #243347; border-radius:10px; padding:20px 22px; margin-bottom:14px;'>
            <div style='display:flex; gap:14px; align-items:flex-start;'>
                <div style='font-size:1.6rem; flex-shrink:0;'>{icon}</div>
                <div style='flex:1;'>
                    <div style='font-family:Space Mono,monospace; font-size:0.88rem; color:#E84855; margin-bottom:8px;'>{title}</div>
                    <div style='font-size:0.82rem; color:#8899AA; line-height:1.6; margin-bottom:10px;'>
                        <b style='color:#F0F4F8;'>Problem: </b>{problem}
                    </div>
                    <div style='font-size:0.82rem; color:#8899AA; line-height:1.6; margin-bottom:10px;'>
                        <b style='color:#3BB273;'>Solution: </b>{solution}
                    </div>
                    <span style='display:inline-block; background:#1A3020; color:#3BB273; border-radius:4px; font-size:0.7rem; padding:2px 8px;'>{tag}</span>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

# ─── PAGE: Key Insights ───────────────────────────────────────────────────────
elif "Insights" in page:
    st.markdown("# 💡 Key Analytical Insights")

    st.markdown("""
    <div class='card card-gold'>
    <p>These insights were derived from Athena SQL queries on the Silver layer and visualised in the Power BI dashboard.
    All findings are based on ~2M ratings (10% stratified sample of the 20M MovieLens dataset).</p>
    </div>
    """, unsafe_allow_html=True)

    insights = [
        ("🎭", "Drama dominates volume but not always quality",
         "Drama has the highest movie count of any genre, but Documentary and Film-Noir genres consistently score higher average ratings despite far fewer titles — quantity ≠ quality."),
        ("📅", "Rating quality peaked in the mid-1990s",
         "The dual-axis year chart reveals a clear quality peak around 1995–2005. Movies per year grew continuously, but average ratings began declining after this 'Golden Era', suggesting audience standards or genre saturation effects."),
        ("💎", "The best movies are often the least seen",
         "Hidden gems — films with avg_rating ≥ 3.8 but fewer than 300 ratings — include critically acclaimed world cinema titles. The mainstream and the excellent rarely overlap."),
        ("📊", "Pre-aggregation reduced Athena costs by ~90%",
         "By computing genre and year aggregations in the ETL layer rather than at query time, Athena scanned pre-aggregated tables of ~20 rows instead of enriched_movies with 27K rows per query."),
        ("🎬", "Blockbusters that are also highly rated are rare",
         "The blockbusters query (total_ratings ≥ 5000 AND avg_rating ≥ 3.8) returns a much smaller subset than either condition alone — popularity and quality are largely independent variables."),
    ]

    for icon, title, desc in insights:
        st.markdown(f"""
        <div class='challenge'>
            <div class='icon'>{icon}</div>
            <div>
                <div class='title' style='color:#E8B84B !important;'>{title}</div>
                <div class='sol'>{desc}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("### Technologies Mastered")
    tech = [
        ("🪣", "Amazon S3", "Data Lake Design"), ("⚙️", "AWS Glue", "Crawler + ETL"),
        ("🔍", "Amazon Athena", "Serverless SQL"), ("📊", "Power BI", "BI Dashboard"),
        ("🐍", "PySpark", "Distributed ETL"), ("🔐", "AWS IAM", "Role Management"),
        ("📋", "SQL", "Query Layer"), ("🎨", "DAX", "BI Measures"),
    ]
    st.markdown('<div class="tech-grid">', unsafe_allow_html=True)
    cols = st.columns(4)
    for i, (icon, name, role) in enumerate(tech):
        with cols[i % 4]:
            st.markdown(f"""
            <div class='tech-item'>
                <div class='t-icon'>{icon}</div>
                <div class='t-name'>{name}</div>
                <div class='t-role'>{role}</div>
            </div>
            """, unsafe_allow_html=True)
