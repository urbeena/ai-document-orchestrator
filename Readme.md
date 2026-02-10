# AI-Powered Document Orchestrator

An AI-powered document orchestration system built using **Streamlit**, **Gemini AI**, and **n8n** to dynamically extract information from documents and automate business workflows such as conditional email notifications.

---

1. User uploads document
2. Streamlit reads text
3. Gemini extracts meaning
4. Python POSTs JSON
5. Webhook receives data
6. IF logic evaluates
7. Email is sent


## 🎯 Project Objective

The goal of this project is to demonstrate:
- Dynamic AI-based document understanding
- Structured information extraction
- Event-driven automation using webhooks
- Business Process Automation (BPA) using n8n

---

## 🧱 Project Architecture (High Level)

---

## 📁 Project Structure

ai-document-orchestrator/
│
├── app.py # Main Streamlit application
├── requirements.txt # Python dependencies
├── README.md # Project documentation
├── .gitignore # Ignored files
│
├── utils/
│ ├── document_reader.py # PDF/TXT document reader
│ ├── gemini_helper.py # (To be added) Gemini AI logic
│ └── n8n_client.py # (To be added) n8n webhook sender
│
└── sample_docs/
└── sample_invoice.txt


---

## ✅ STEP 1: Environment Setup

### What was done:
- Created a Python virtual environment (`venv`)
- Activated the environment
- Selected the environment in VS Code
- Installed required libraries
- Added `venv/` and `.env` to `.gitignore`

### Why:
- To isolate project dependencies
- To avoid version conflicts
- To follow industry best practices

---

## ✅ STEP 2: Basic Streamlit Application

### What was done:
- Created a basic Streamlit app (`app.py`)
- Added a file uploader for PDF and TXT files
- Verified the app runs locally

### Outcome:
- Streamlit UI loads correctly
- User can upload a document

---

## ✅ STEP 3: Document Reading (PDF / TXT)

### What was done:
- Implemented document reading logic in `utils/document_reader.py`
- Supported both `.txt` and `.pdf` files
- Displayed extracted text preview in the Streamlit UI

### Outcome:
- Uploaded documents are successfully converted into plain text
- Text is ready to be sent to an AI model for analysis

---

## 🧠 Next Steps (Planned)

- Integrate **Gemini AI** for document understanding
- Extract structured information (JSON)
- Send AI output to **n8n** via webhook
- Implement conditional email automation
- Deploy application using **Streamlit Cloud**

---

## 🚀 Tech Stack

- **Frontend**: Streamlit
- **Backend**: Python
- **AI Model**: Gemini API
- **Automation**: n8n
- **Version Control**: Git & GitHub