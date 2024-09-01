import os
from dotenv import load_dotenv
from pdf_splitter import split_pdf


def main():
    folder_path = get_folder_path()

    pdf_filename = os.getenv('PDF_NAME')
    pdf_path = os.path.join(folder_path, pdf_filename)

    split_pdf(pdf_path, folder_path)


def get_folder_path():
    load_dotenv()
    return os.path.expanduser(os.getenv('FOLDER_PATH'))


if __name__ == '__main__':
    main()
