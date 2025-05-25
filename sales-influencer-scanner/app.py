import streamlit as st
import pandas as pd
from utils import extract_pdf_metrics
from predictor import predict_sales, calculate_sales_score

st.set_page_config(page_title="Sales Influencer Scanner", layout="centered")
st.title("📊 Sales Influencer Scanner")
st.markdown("Upload a HypeAuditor PDF and discover hidden sales power.")

uploaded_file = st.file_uploader("Upload HypeAuditor PDF", type=["pdf"])
all_data = []

if uploaded_file is not None:
    with st.spinner("Processing PDF..."):
        metrics = extract_pdf_metrics(uploaded_file)
        if metrics:
            sales_prediction = predict_sales(metrics)
            sales_score = calculate_sales_score(metrics)
            metrics['Predicted Monthly Sales (USD)'] = f"${sales_prediction:,.2f}"
            metrics['Sales Influencer Score'] = round(sales_score, 2)
            st.success(f"📈 Estimated Monthly Sales: **${sales_prediction:,.2f}**")
            st.info(f"🔥 Sales Influencer Score™: **{round(sales_score, 2)}**")
            df = pd.DataFrame(metrics.items(), columns=['Metric', 'Value'])
            st.subheader("📋 Extracted Metrics")
            st.table(df)
            all_data.append(metrics)

            # CSV download
            csv = pd.DataFrame([metrics]).to_csv(index=False).encode('utf-8')
            st.download_button("📥 Download as CSV", data=csv, file_name="influencer_sales_prediction.csv")
        else:
            st.error("❌ Could not extract metrics. Please try another PDF.")
