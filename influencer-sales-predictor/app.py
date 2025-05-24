import streamlit as st
from utils import extract_pdf_metrics
from predictor import predict_sales

st.set_page_config(page_title="Influencer Sales Predictor", layout="centered")
st.title("📊 Influencer Sales Predictor")
st.markdown("Upload a HypeAuditor PDF and get an estimated monthly sales potential.")

uploaded_file = st.file_uploader("Upload HypeAuditor PDF", type=["pdf"])

if uploaded_file is not None:
    with st.spinner("Extracting data and predicting..."):
        metrics = extract_pdf_metrics(uploaded_file)
        if metrics:
            prediction = predict_sales(metrics)
            st.success(f"Estimated Monthly Sales: **${prediction:,.2f}**")
            st.subheader("🔍 Key Metrics")
            for key, value in metrics.items():
                st.markdown(f"- **{key}**: {value}")
        else:
            st.error("Could not extract metrics. Please check PDF format.")
