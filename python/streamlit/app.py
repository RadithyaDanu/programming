import streamlit as st
import pandas as pd
import plotly.express as px

# ---------- Konfigurasi Halaman ----------
st.set_page_config(
    page_title="Dashboard Penjualan",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------- Custom CSS ----------
st.markdown(
    """
    <style>
    /* Font & background */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1200px;
    }

    /* Header */
    div[data-testid="stHeader"] {
        background: transparent;
    }

    /* Kartu metric */
    div[data-testid="stMetric"] {
        background: linear-gradient(135deg, #1A1F2E 0%, #232A3D 100%);
        border: 1px solid rgba(108, 99, 255, 0.25);
        border-radius: 16px;
        padding: 20px 24px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }

    div[data-testid="stMetric"]:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 28px rgba(108, 99, 255, 0.25);
    }

    div[data-testid="stMetric"] label {
        color: #A8B1C4 !important;
        font-weight: 600;
    }

    div[data-testid="stMetric"] value {
        color: #FAFAFA;
        font-weight: 700;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background: #12151F;
        border-right: 1px solid rgba(108, 99, 255, 0.15);
    }

    /* Tombol */
    .stButton > button {
        border-radius: 10px;
        border: 1px solid #6C63FF;
        background: linear-gradient(135deg, #6C63FF 0%, #9B8CFF 100%);
        color: white;
        font-weight: 600;
        transition: all 0.2s ease;
    }

    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 18px rgba(108, 99, 255, 0.4);
    }

    /* Judul section */
    .section-title {
        color: #FAFAFA;
        font-size: 1.4rem;
        font-weight: 700;
        margin: 1.5rem 0 1rem 0;
        padding-bottom: 0.5rem;
        border-bottom: 2px solid rgba(108, 99, 255, 0.4);
        display: inline-block;
    }

    /* Badge tanggal */
    .date-badge {
        display: inline-block;
        background: rgba(108, 99, 255, 0.15);
        color: #9B8CFF;
        padding: 4px 14px;
        border-radius: 999px;
        font-size: 0.85rem;
        font-weight: 600;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------- Data Dummy ----------
@st.cache_data
def load_data():
    df = pd.DataFrame(
        {
            "tanggal": pd.date_range("2026-01-01", periods=180, freq="D"),
        }
    )
    import numpy as np

    rng = np.random.default_rng(42)
    df["penjualan"] = (
        100
        + np.cumsum(rng.normal(0.5, 8, len(df)))
        + 20 * np.sin(np.arange(len(df)) * 2 * np.pi / 7)
    ).round(0)
    df["transaksi"] = rng.integers(40, 120, len(df))
    df["hari"] = df["tanggal"].dt.day_name()
    return df


df = load_data()

# ---------- Sidebar ----------
with st.sidebar:
    st.markdown("### 📊 Dashboard")
    st.markdown("---")

    st.markdown("#### Filter")

    rentang_tanggal = st.date_input(
        "Rentang Tanggal",
        value=(df["tanggal"].min().date(), df["tanggal"].max().date()),
        min_value=df["tanggal"].min().date(),
        max_value=df["tanggal"].max().date(),
    )

    hari_pilihan = st.multiselect(
        "Pilih Hari",
        options=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
        default=[],
        placeholder="Semua hari (default)",
    )

    st.markdown("---")
    if st.button("🔄 Refresh Data", use_container_width=True):
        st.cache_data.clear()
        st.rerun()

# ---------- Filter Data ----------
mask = pd.Series(True, index=df.index)
if len(rentang_tanggal) == 2:
    mask &= df["tanggal"].dt.date.between(rentang_tanggal[0], rentang_tanggal[1])
if hari_pilihan:
    mask &= df["hari"].isin(hari_pilihan)

df_filtered = df[mask].copy()

if df_filtered.empty:
    st.warning("⚠️ Tidak ada data untuk filter yang dipilih. Coba ubah filternya.")
    st.stop()

# ---------- Header ----------
st.markdown(
    f"""
    <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:1rem;">
        <div>
            <h1 style="margin:0; font-size:2.2rem; font-weight:700;">
                Dashboard Penjualan 📈
            </h1>
            <p style="margin:0.3rem 0 0 0; color:#A8B1C4;">
                Analisis performa penjualan harian interaktif
            </p>
        </div>
        <span class="date-badge">{df_filtered['tanggal'].min().strftime('%d %b %Y')} — {df_filtered['tanggal'].max().strftime('%d %b %Y')}</span>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown("<br>", unsafe_allow_html=True)

# ---------- Metric Cards ----------
total_penjualan = df_filtered["penjualan"].sum()
total_transaksi = df_filtered["transaksi"].sum()
rata_penjualan = df_filtered["penjualan"].mean()
hari_terbaik = df_filtered.groupby("hari")["penjualan"].sum().idxmax()

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Penjualan", f"{total_penjualan:,.0f}", delta="12.5%")
with col2:
    st.metric("Total Transaksi", f"{total_transaksi:,}", delta="8.2%", delta_color="normal")
with col3:
    st.metric("Rata-rata Harian", f"{rata_penjualan:,.0f}", delta="-2.1%")
with col4:
    st.metric("Hari Terbaik", hari_terbaik)

# ---------- Charts ----------
st.markdown('<span class="section-title">Tren Penjualan</span>', unsafe_allow_html=True)

tab1, tab2 = st.tabs(["📈 Line Chart", "📊 Bar Chart"])

with tab1:
    fig_line = px.line(
        df_filtered,
        x="tanggal",
        y="penjualan",
        title="Penjualan Harian",
        color_discrete_sequence=["#6C63FF"],
    )
    fig_line.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#FAFAFA"),
        title_x=0.02,
        height=420,
        xaxis=dict(gridcolor="rgba(255,255,255,0.08)", showgrid=True),
        yaxis=dict(gridcolor="rgba(255,255,255,0.08)", showgrid=True),
        hovermode="x unified",
    )
    fig_line.update_traces(line_width=2.5, fill="tozeroy", fillcolor="rgba(108,99,255,0.12)")
    st.plotly_chart(fig_line, use_container_width=True)

with tab2:
    harian = df_filtered.groupby("hari", observed=True)["penjualan"].sum().reindex(
        ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    ).dropna()
    fig_bar = px.bar(
        x=harian.index,
        y=harian.values,
        title="Total Penjualan per Hari",
        color=harian.values,
        color_continuous_scale=["#6C63FF", "#9B8CFF"],
    )
    fig_bar.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#FAFAFA"),
        title_x=0.02,
        height=420,
        xaxis=dict(gridcolor="rgba(255,255,255,0.08)", title=None),
        yaxis=dict(gridcolor="rgba(255,255,255,0.08)", title="Penjualan"),
        coloraxis_showscale=False,
    )
    fig_bar.update_traces(marker_line_width=0)
    st.plotly_chart(fig_bar, use_container_width=True)

# ---------- Data Table ----------
st.markdown('<span class="section-title">Data Detail</span>', unsafe_allow_html=True)

df_tampil = df_filtered.copy()
df_tampil["tanggal"] = df_tampil["tanggal"].dt.strftime("%d %b %Y")
df_tampil = df_tampil.rename(
    columns={"tanggal": "Tanggal", "penjualan": "Penjualan", "transaksi": "Transaksi", "hari": "Hari"}
)

st.dataframe(
    df_tampil,
    use_container_width=True,
    height=350,
    hide_index=True,
    column_config={
        "Penjualan": st.column_config.NumberColumn(format="%,.0f"),
    },
)

st.markdown(
    """
    <div style="text-align:center; color:#6B7280; margin-top:2rem; font-size:0.85rem;">
        Dibuat dengan Streamlit · Data dummy untuk belajar
    </div>
    """,
    unsafe_allow_html=True,
)
