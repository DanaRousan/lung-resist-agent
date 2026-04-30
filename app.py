import streamlit as st
from agent import generate_inference

st.set_page_config(page_title="Genomic Reasoning Agent", layout="wide")

st.title("🧬 Evidence-Driven Genomic Reasoning Agent")
st.subheader("NSCLC Resistance Inference: EGFR, HER2, MET")
st.markdown("---")

col1, col2 = st.columns([1, 2])

with col1:
    st.markdown("### 📋 Patient Input")
    patient_text = st.text_area(
        "Enter Genomic Profile:",
        height=150,
        placeholder="e.g., 65yo female, HER2-mutant NSCLC progressing on T-DXd. NGS shows SLFN11 loss."
    )
    
    analyze_button = st.button("Generate Resistance Inference", type="primary")
    
    st.markdown("### 🛡️ System Guardrails")
    st.info("**Risk Tier:** Moderate (Advisory)\n\n**Oversight:** Human-in-the-loop required. Adheres to DKITE clinical AI methodology.")

with col2:
    st.markdown("### 📊 Ranked Resistance Report")
    if analyze_button and patient_text:
        with st.spinner("Retrieving evidence and reasoning..."):
            try:
                report = generate_inference(patient_text)
                st.success("Inference Complete")
                st.markdown(report)
            except Exception as e:
                st.error(f"System Error. Did you add the API Key to Streamlit Secrets? Details: {e}")
    elif not analyze_button:
        st.write("Awaiting patient input...")
