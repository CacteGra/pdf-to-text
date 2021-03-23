import glob
from pdf2image import convert_from_path
import pytesseract
from PIL import Image
import pathlib
import os
from decouple import config

pdf_path = input('Please provide the path to pdfs folder: ')
if list(pdf_path)[-1] == " ":
    pdf_path = pdf_path[:-1]
    pdf_path = pdf_path.replace('\\', '')
print(pdf_path)
with open(r'{}/full_text.txt'.format(pdf_path), 'w'):
    pass

pytesseract.pytesseract.tesseract_cmd = config('TESSERACT_PATH')

for pdf_file in glob.glob('{}/*.pdf'.format(pdf_path)):
    print('after')
    print(pdf_file)
    # Load your PDF

    pages = convert_from_path('{1}'.format(pdf_path, pdf_file), 350)

    i = 0
    for page in pages:
        file_name = pdf_file.replace('.pdf', '')
        page.save("pdf_image_{}.jpg".format(i), "JPEG")
        i = i+1

        for n in range(i):
            image_name = 'pdf_image_{}.jpg'.format(n)
            image = Image.open(image_name)
            image_to_text = pytesseract.image_to_string(image, lang='eng')

            # Print the text
            print(image_to_text)

            with open(r'{}/full_text.txt'.format(pdf_path), 'a') as full_text:
                full_text.write(image_to_text)

    with open(r'{}/full_text.txt'.format(pdf_path), 'a') as full_text:
        full_text.write('\n')
