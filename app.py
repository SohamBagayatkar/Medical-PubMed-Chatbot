import streamlit as st

st.set_page_config(
    page_title="Medical PubMed Analysis",
    page_icon="🩺",
    layout="wide"
)

with st.sidebar:
    st.image("https://s3ktech.ai/wp-content/uploads/2025/03/S3Ktech-Logo.png", width=140)

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700&display=swap');

    html, body, [class*="st-"] {
        font-family: 'Roboto', sans-serif;
    }
    h1, h2, h3, h4, h5, h6 {
        font-weight: 700;
        color: #2c3e50; /* Darker heading color */
    }
    .stButton>button {
        background-color: #3498db; /* Blue button */
        color: white;
        border-radius: 8px;
        border: none;
        padding: 10px 20px;
        font-size: 16px;
        cursor: pointer;
        transition: background-color 0.3s ease;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .stButton>button:hover {
        background-color: #2980b9; /* Darker blue on hover */
    }
    .stAlert {
        border-radius: 8px;
        box_shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
    }
    .stMarkdown {
        line-height: 1.6;
        font-size: 1.1em;
    }
    .stTextInput>div>div>input {
        border-radius: 8px;
        border: 1px solid #ced4da;
        padding: 10px;
    }
    .css-1d391kg.e16z5zjs3 {
        background-color: #f8f9fa; /* Light gray background for sidebar */
        padding: 20px;
        border-right: 1px solid #e9ecef;
    }
    .main .block-container {
        padding-top: 3rem;
        padding-bottom: 3rem;
    }
    .footer {
        font-size: 0.9em;
        color: #6c757d;
        text-align: center;
        margin-top: 40px;
        padding-top: 20px;
        border-top: 1px solid #e9ecef;
    }
</style>
"""
, unsafe_allow_html=True)

st.title("🩺 Medical PubMed Analysis Tool")
st.markdown("""
    A comprehensive tool for analyzing medical research articles from PubMed.
    Streamline your literature review, data extraction, and report generation.
"""
)

st.markdown("""
## Welcome to the Medical PubMed Analysis Tool

This tool helps you analyze medical research articles from PubMed in a structured way. Follow these steps:

### Step 1: Search on PubMed
1. Go to [PubMed](https://pubmed.ncbi.nlm.nih.gov/)
2. Perform your search
3. Save the results as a text file (use the 'Save' button on PubMed)

### Step 2: Upload and Process
1. Go to the "Evidence Analysis" page
2. Upload your saved PubMed results
3. Click "Process Articles" to analyze the content

### Step 3: Explore the Results
The tool will generate:
- Overall evidence summary
- Metadata table
- Individual article summaries
- Comparative analysis
- Clinical conclusions

### Step 4: Visualize Data
Visit the "Data Visualization" page to see:
- Healing rates comparison
- Adverse event rates
- Time to symptom relief
- Drug interaction risks

### Step 5: Generate Clinical Documents
The "Clinical Documents" page provides:
- Clinical Trial Protocol Introduction (ICH M11 format)
- Clinical Study Report Discussion (TransCelerate format)

## Getting Started
Click on "Evidence Analysis" in the sidebar to begin!
"""
)

st.markdown("""
<div class="footer">
    © 2024 S3K Technologies | All rights reserved
</div>
"""
, unsafe_allow_html=True)
