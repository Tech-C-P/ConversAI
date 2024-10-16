from src.components.loaders.websiteCrawler import WebsiteCrawler
from src.components.loaders.youtubeLoader import YoutubeTranscriptLoader
from src.components.loaders.pdfLoader import PdfLoader
from src.components.rag.RAG import Chain

class Pipeline:
    def __init__(self):
        """Initialize the Pipeline with loaders and the RAG chain."""
        self.pdfLoader = PdfLoader()
        self.webCrawler = WebsiteCrawler()
        self.youtubeLoader = YoutubeTranscriptLoader()
        self.ragChain = Chain()

    def plainText(self, text: str):
        """
        Process plain text through the RAG chain.

        Args:
            text (str): The input text to process.

        Returns:
            Chain: The processed chain for the input text.
        """
        chain = self.ragChain.returnChain(text=text)
        return chain

    def searchablePdf(self, path: str):
        """
        Process a searchable PDF file.

        Args:
            path (str): The path to the PDF file.

        Returns:
            Chain: The processed chain from the extracted text.
        """
        extractedText = self.pdfLoader.searchablePdf(pdfPath=path)
        chain = self.ragChain.returnChain(text=extractedText)
        return chain

    def scannablePdf(self, path: str):
        """
        Process a scannable PDF file.

        Args:
            path (str): The path to the PDF file.

        Returns:
            Chain: The processed chain from the extracted text.
        """
        extractedText = self.pdfLoader.scannablePdf(pdfPath=path)
        chain = self.ragChain.returnChain(text=extractedText)
        return chain
    
    def webCrawl(self, urls: list[str]):
        """
        Crawl the web for text extraction from provided URLs.

        Args:
            urls (list[str]): A list of URLs to crawl.

        Returns:
            Chain: The processed chain from the extracted text.
        """
        extractedText = self.webCrawler.extractTextFromUrlList(urls=urls)
        chain = self.ragChain.returnChain(text=extractedText)
        return chain     
    
    def youtubeLinks(self, urls: list[str]):
        """
        Extract transcripts from YouTube links.

        Args:
            urls (list[str]): A list of YouTube video URLs.

        Returns:
            Chain: The processed chain from the extracted transcripts.
        """
        extractedText = self.youtubeLoader.getTranscripts(urls=urls)
        chain = self.ragChain.returnChain(text=extractedText)
        return chain