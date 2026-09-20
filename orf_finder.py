import streamlit as st

def render_orf_finder():
    st.header("ORF Finder")
    dna_input = st.text_area("Enter DNA sequence:", key="orf_dna")
    if st.button("Find ORFs", key="orf_btn"):
        clean_seq = dna_input.upper().replace(" ", "").replace("\n", "")
        start_codon, stop_codons, orfs = "ATG", ["TAA", "TAG", "TGA"], []
        for frame in range(3):
            for i in range(frame, len(clean_seq) - 2, 3):
                if clean_seq[i:i+3] == start_codon:
                    for j in range(i + 3, len(clean_seq) - 2, 3):
                        if clean_seq[j:j+3] in stop_codons:
                            seq = clean_seq[i:j+3]
                            if len(seq) >= 30:
                                orfs.append((frame + 1, i + 1, j + 3, seq))
                            break
        if orfs:
            for frame, start, end, seq in orfs:
                st.write(f"**Frame {frame}:** Start {start}, End {end}, Length {len(seq)} bp")
        else:
            st.info("No potential ORFs found.")