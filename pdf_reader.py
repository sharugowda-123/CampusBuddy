import PyPDF2

def extract_text_from_pdf(pdf_path):
    """
    A simple function to extract text from a PDF file.
    """
    text = ""
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            num_pages = len(reader.pages)
            for page_num in range(num_pages):
                page = reader.pages[page_num]
                text += page.extract_text() + "\n"
        return text
    except Exception as e:
        return f"Error reading PDF: {str(e)}"

# Example usage: Extract text from a sample PDF
if __name__ == "__main__":
    extracted_text = extract_text_from_pdf("sample_circular.pdf")
    print(extracted_text[:500]) # Print first 500 characters