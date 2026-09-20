import streamlit as st

# Import renderers from modular files
from gc_calculator import render_gc_calculator
from dna_translator import render_dna_translator
from orf_finder import render_orf_finder
from bacterial_simulator import render_bacterial_simulator

# Page Config
st.set_page_config(
    page_title="Bioinformatics Dashboard",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Custom Styling
st.markdown(
    """
    <style>
    /* Main Background & Fonts */
    .main {
        background-color: #0f172a;
        color: #f8fafc;
    }
    
    /* Centered Header Container */
    .header-box {
        background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
        border: 1px solid #334155;
        border-radius: 12px;
        padding: 32px 24px;
        margin-bottom: 30px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.25);
        text-align: center; /* Centers the content */
    }
    
    .header-title {
        color: #38bdf8;
        font-size: 2.5rem; /* Made slightly larger to stand out */
        font-weight: 700;
        margin-bottom: 12px;
    }
    
    .header-sub {
        color: #94a3b8;
        font-size: 1.1rem;
    }

    /* Card Styling */
    div[data-testid="stVerticalBlock"] > div[data-testid="stBlock"] {
        border-radius: 10px;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# Header Section (Centered and Highlighted)
st.markdown(
    """
    <div class="header-box">
        <div class="header-title">🧬 Bioinformatics & Analysis Suite</div>
        <div class="header-sub">Modular workspace for sequence processing and bacterial growth analytics</div>
    </div>
""",
    unsafe_allow_html=True,
)

# Grid Layout: Row 1
col1, col2 = st.columns(2, gap="medium")

with col1:
    with st.container(border=True):
        # Added emoji and a hover tooltip using the native help parameter
        st.subheader("🧬 GC Content Calculator", help="Calculate the percentage of guanine (G) and cytosine (C) bases in a raw or FASTA DNA sequence.")
        render_gc_calculator()

with col2:
    with st.container(border=True):
        # Added emoji and a hover tooltip using the native help parameter
        st.subheader("🧬 DNA to Protein Translator", help="Transcribes and translates a DNA nucleotide sequence into its corresponding amino acid chain.")
        render_dna_translator()

st.write("")  # Spacing

# Grid Layout: Row 2 (Fixed layout columns)
col3, col4 = st.columns(2, gap="medium")

with col3:
    with st.container(border=True):
        # Added emoji and a hover tooltip using the native help parameter
        st.subheader("🔍 ORF Finder", help="Locate Open Reading Frames (ORFs) to identify potential protein-coding segments within a sequence.")
        render_orf_finder()

with col4:
    with st.container(border=True):
        # Added emoji and a hover tooltip using the native help parameter
        st.subheader("🧫 Universal Bacterial Growth Curve Analyzer", help="Upload lab spreadsheets (.xlsx, .csv) to model growth kinetics and visualize automated metrics.")
        render_bacterial_simulator()
