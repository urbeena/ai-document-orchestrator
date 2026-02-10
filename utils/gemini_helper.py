import os
import json
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def extract_document_info(text: str) -> dict:
    prompt = f"""
You are an AI document analyzer.

From the document text below:
1. Identify document type (invoice, resume, legal, academic, other)
2. Extract key fields
3. Provide a short summary

Return ONLY valid JSON in this format:
{{
  "document_type": "",
  "key_fields": {{}},
  "summary": ""
}}

Document Text:
{text}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You output ONLY valid JSON."},
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )

    raw_output = response.choices[0].message.content.strip()

    # Safety: ensure JSON parsing
    try:
        return json.loads(raw_output)
    except json.JSONDecodeError:
        return {
            "error": "Invalid JSON returned by model",
            "raw_output": raw_output
        }
