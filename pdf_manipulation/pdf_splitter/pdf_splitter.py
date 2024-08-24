from PyPDF2 import PdfReader, PdfWriter
import os


def split_pdf(pdf_path, page_number, folder_path):
    with open(pdf_path, 'rb') as pdf_file:
        reader = PdfReader(pdf_file)

        for page in reader.pages:
            writer_current_page = PdfWriter()
            writer_current_page.add_page(page)

            output_current_page = os.path.join(folder_path, f'Page-{page_number + 1}.pdf')

            with open(output_current_page, 'wb') as pdf_output:
                writer_current_page.write(pdf_output)

            page_number += 1

    print('PDF successfully split.')
