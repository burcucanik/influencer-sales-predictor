import streamlit as st
from PyPDF2 import PdfReader
import pytesseract
from pdf2image import convert_from_path
from PIL import Image
import tempfile
import os

def extract_text_from_pdf(file):
    temp_dir = tempfile.mkdtemp()
    images = convert_from_path(file, output_folder=temp_dir, fmt='png')
    full_text = ""
    for image in images:
        text = pytesseract.image_to_string(image)
        full_text += text + "\n"
    return full_text

def parse_metrics(text):
    metrics = {
        "Followers": None,
        "Engagement Rate": None,
        "Authentic Engagement": None,
        "Reach": None,
        "Audience Quality Score (AQS)": None,
        "Top Country": None,
    }
    for line in text.splitlines():
        for key in metrics.keys():
            if key.lower() in line.lower():
                try:
                    parts = line.split()
                    value = parts[-1].replace(",", "").replace("%", "")
                    metrics[key] = float(value) if value.replace(".", "").isdigit() else value
                except:
                    metrics[key] = "?"
    return metrics

st.title("📊 Influencer Sales Predictor (OCR-based)")

uploaded_file = st.file_uploader("Upload HypeAuditor PDF", type="pdf")

if uploaded_file is not None:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(uploaded_file.read())
        tmp_path = tmp_file.name

    st.info("Extracting data with OCR, please wait...")
    extracted_text = extract_text_from_pdf(tmp_path)
    metrics = parse_metrics(extracted_text)

    st.subheader("Extracted Metrics")
    for k, v in metrics.items():
        st.write(f"**{k}**: {v}")

    st.subheader("Predicted Monthly Sales")
    try:
        # Example: very naive logic just for demonstration
        followers = float(metrics.get("Followers", 0))
        engagement = float(metrics.get("Engagement Rate", 0))
        aqs = float(metrics.get("Audience Quality Score (AQS)", 0))
        prediction = round((followers * engagement * aqs) / 10000, 2)
        st.success(f"Estimated Monthly Sales: ${prediction}")
    except:
        st.warning("Insufficient or invalid data to calculate sales.")
