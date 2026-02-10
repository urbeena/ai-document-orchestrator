from PyPDF2 import PdfReader

def read_pdf_file(uploaded_file):
     """ Reads text from a .pdf file """ 
     reader = PdfReader(uploaded_file) 
     text = ""
     for page in reader.pages:
        page_text = page.extract_text() 
        if page_text:
            text += page_text + "\n"
        return text



def read_txt_file(uploaded_file):
     """ Reads text from a .txt file """ 
     return uploaded_file.read().decode("utf-8")
