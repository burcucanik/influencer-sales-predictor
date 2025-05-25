import fitz  # PyMuPDF

def extract_pdf_metrics(uploaded_file):
    try:
        with fitz.open(stream=uploaded_file.read(), filetype="pdf") as doc:
            text = "\n".join(page.get_text() for page in doc)

        def find(pattern):
            for line in text.split('\n'):
                if pattern.lower() in line.lower():
                    return line.split()[-1]
            return None

        return {
            "Followers": find("Followers") or "0",
            "Engagement Rate": find("Engagement Rate") or "0%",
            "Authentic Engagement": find("Authentic Engagement") or "0",
            "Reach": find("Estimated Reach") or "0",
            "Audience Quality Score (AQS)": find("AQS") or "0",
            "Top Country": find("Top Country") or "Unknown"
        }
    except Exception as e:
        print("PDF extraction error:", e)
        return None
