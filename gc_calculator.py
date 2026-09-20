import streamlit as st

def render_gc_calculator():
    st.header("GC Content Calculator")
    dna_input = st.text_area("Enter DNA sequence:", key="gc_dna")
    if st.button("Calculate GC", key="gc_btn"):
        clean_seq = dna_input.upper().replace(" ", "").replace("\n", "")
        total = len(clean_seq)
        gc_count = clean_seq.count("G") + clean_seq.count("C")
        gc_percent = round((gc_count / total) * 100, 2) if total > 0 else 0.0
        st.success(f"GC Content: {gc_percent}%")