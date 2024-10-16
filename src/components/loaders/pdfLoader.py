from src.utils.functions import cleanText, getConfig
from concurrent.futures import ThreadPoolExecutor
from src.utils.exceptions import CustomException
from pdf2image import convert_from_path
from src.utils.logging import logger
import numpy as np
import pymupdf
import easyocr

class PdfLoader:
    def __init__(self) -> None:
        """
        Initialize the PdfLoader with configuration settings and an EasyOCR reader.
        """
        self.config = getConfig(path="config.ini") 
        self.reader = easyocr.Reader(['en'], gpu=self.config.getboolean("EASYOCR", "gpu"))

    def extractTextFromPage(self, page) -> str:
        """
        Extract and clean text from a PDF page.

        Args:
            page: A PyMuPDF page object.

        Returns:
            str: Cleaned text extracted from the page.
        """
        return cleanText(text=page.get_text())

    def searchablePdf(self, pdfPath: str) -> str:
        """
        Extract text from a searchable PDF.

        Args:
            pdfPath (str): The file path to the searchable PDF.

        Returns:
            str: All extracted text from the PDF.
        """
        try:
            logger.info("Text Extraction Started from Searchable PDF")
            doc = pymupdf.open(pdfPath)
            pages = [doc.load_page(i) for i in range(len(doc))]
            with ThreadPoolExecutor() as executor:
                texts = list(executor.map(self.extractTextFromPage, pages))
            doc.close()
            return "\n".join(texts)
        except Exception as e:
            logger.error(CustomException(e))

    def getText(self, image) -> str:
        """
        Extract and clean text from an image using EasyOCR.

        Args:
            image: An image (numpy array).

        Returns:
            str: Cleaned text extracted from the image.
        """
        text = "\n".join([text[1] for text in self.reader.readtext(np.array(image), paragraph=True)])
        return cleanText(text=text)

    def scannablePdf(self, pdfPath: str) -> str:
        """
        Extract text from a scannable PDF using OCR.

        Args:
            pdfPath (str): The file path to the scannable PDF.

        Returns:
            str: All extracted text from the PDF.
        """
        try:
            logger.info("Text Extraction Started from Scannable PDF")
            allImages = convert_from_path(pdfPath)
            texts = [self.getText(image) for image in allImages]
            return "\n".join(texts)
        except Exception as e:
            logger.error(CustomException(e))