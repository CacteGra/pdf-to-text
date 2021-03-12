import glob
import pdftotext

full_text = ''

for pdf_file in glob.iglob('.pdf'):
    # Load your PDF
    with open(pdf_file, "rb") as f:
        pdf = pdftotext.PDF(f)

        # Iterate over all the pages
        for page in pdf:
            if full_text:
                full_text += '\n' + page
            else:
                full_text = page
            print(page)