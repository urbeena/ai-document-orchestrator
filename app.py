import streamlit as st
from utils.document_reader import read_pdf_file, read_txt_file
from utils.test_gemini import extract_document_info
from utils.webhook_client import post_to_n8n

st.title("AI Document Orchestrator")

# Initialize session state
if "document_text" not in st.session_state:
    st.session_state.document_text = None

if "analysis_result" not in st.session_state:
    st.session_state.analysis_result = None


# 1️⃣ Upload document
uploaded_file = st.file_uploader(
    "Upload a document (PDF or TXT)", type=["pdf", "txt"]
)

if uploaded_file:
    if uploaded_file.type == "application/pdf":
        st.session_state.document_text = read_pdf_file(uploaded_file)
    elif uploaded_file.type == "text/plain":
        st.session_state.document_text = read_txt_file(uploaded_file)

    st.success("Document uploaded successfully!")


# 2️⃣ Run Gemini analysis
if st.session_state.document_text:
    if st.button("Run Gemini Analysis"):
        with st.spinner("Analyzing document..."):
            st.session_state.analysis_result = extract_document_info(
                st.session_state.document_text
            )
        st.success("Document analysis complete!")
        st.json(st.session_state.analysis_result)


# 3️⃣ Send to n8n
if st.session_state.analysis_result:
    if st.button("Send to n8n"):
        with st.spinner("Sending data to n8n..."):
            response = post_to_n8n(st.session_state.analysis_result)

        if response.status_code == 200:
            st.success("Data successfully sent to n8n 🎉")
        else:
            st.error(f"n8n error: {response.status_code}")
