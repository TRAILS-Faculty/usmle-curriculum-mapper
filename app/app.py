import streamlit as st
from nlp_engine import analyze_pdf
from report_generator import generate_reports

st.set_page_config(page_title="USMLE Curriculum Mapper", layout="wide")

st.title("📘 USMLE Curriculum Mapping Tool")

pdf_file = st.file_uploader("Upload a session PDF", type=["pdf"])

if st.button("Analyze") and pdf_file is not None:
    with st.spinner("Extracting text and analyzing USMLE alignment..."):
        results_df, summary_df = analyze_pdf(pdf_file)

    st.success("Analysis complete!")

    st.subheader("Coverage Summary")
    st.dataframe(summary_df, use_container_width=True)

    docx_file, excel_file = generate_reports(results_df, summary_df)
    st.download_button("Download Word report", docx_file, "usmle_report.docx")
    st.download_button("Download Excel report", excel_file, "usmle_report.xlsx")
