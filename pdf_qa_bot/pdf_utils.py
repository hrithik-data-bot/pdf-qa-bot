"""Utilities for reading and writing PDFs"""

from PyPDF2 import PdfReader


class PDFUtils:
    """Class for PDF utilities"""


    def __init__(self, pdf_path: str) -> None:
        """Initialize PDFUtils with a given PDF file path"""

        self.pdf_path = pdf_path
        self.pdf_reader = PdfReader(self.pdf_path)
        self.num_pages = len(self.pdf_reader.pages)


    def extract_text(self, page_number: int) -> str:
        """Extract the text from provided page number"""

        if page_number < 0 or page_number >= self.num_pages:
            raise IndexError(f"Page number {page_number} is out of range. Total pages: {self.num_pages}")

        page = self.pdf_reader.pages[page_number]
        text = page.extract_text()
        return text
