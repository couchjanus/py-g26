import pdfplumber

path = 'invoice.pdf'

with pdfplumber.open(path) as pdf:
    pages = pdf.pages
    
    for page in pages:
        with open('invoice.txt', 'a') as f:
            text = page.extract_text()
            print(text)
            f.write(text)