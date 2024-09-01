import os
import unittest
from unittest.mock import patch, MagicMock
from pdf_manipulation.pdf_splitter import split_pdf


class TestPdfSplitter(unittest.TestCase):

    @patch('pdf_manipulation.pdf_splitter.pdf_splitter.PdfReader')
    @patch('pdf_manipulation.pdf_splitter.pdf_splitter.PdfWriter')
    @patch('pdf_manipulation.pdf_splitter.pdf_splitter.open', new_callable=unittest.mock.mock_open)
    def test_split_pdf(self, mock_open, mock_pdf_writer, mock_pdf_reader):
        # SetUp PdfReader Mock
        mock_pdf = MagicMock
        mock_pdf.pages = [MagicMock(), MagicMock(), MagicMock()]
        mock_pdf_reader.return_value = mock_pdf

        # SetUp PdfWriter Mock
        mock_writer = MagicMock()
        mock_pdf_writer.return_value = mock_writer

        # SetUp fictional PDF file
        pdf_path = 'dummy.pdf'
        folder_path = 'output_folder'

        # Calling split_pdf
        split_pdf(pdf_path, folder_path)

        # Checking if the open function was called correctly
        calls = [
            unittest.mock.call(os.path.join(folder_path, 'Page-1.pdf'), 'wb'),
            unittest.mock.call(os.path.join(folder_path, 'Page-2.pdf'), 'wb'),
            unittest.mock.call(os.path.join(folder_path, 'Page-3.pdf'), 'wb')
        ]

        mock_open.assert_has_calls(calls, any_order=True)

        # Checking if the write method was called 3 times (once for each page)
        self.assertEqual(mock_writer.write.call_count, 3)

        # Checking if the pages were added correctly
        self.assertEqual(mock_writer.add_page.call_count, 3)


if __name__ == '__main__':
    unittest.main()
