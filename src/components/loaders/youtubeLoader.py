from langchain_community.document_loaders import YoutubeLoader
from src.utils.exceptions import CustomException
from src.utils.functions import cleanText
from src.utils.logging import logger

class YoutubeTranscriptLoader:
    def __init__(self):
        """Initialize the YoutubeTranscriptLoader."""
        pass
        
    def getTranscripts(self, urls: str) -> str:
        """
        Retrieve transcripts from a list of YouTube URLs.

        Args:
            urls (str): Comma-separated YouTube URLs to fetch transcripts from.

        Returns:
            str: Combined transcripts cleaned and joined by newlines.
        """
        texts = []
        for url in set(urls):
            try:
                loader = YoutubeLoader.from_youtube_url(url, add_video_info=False)
                doc = " ".join([x.page_content for x in loader.load()])
                texts.append(cleanText(text=doc))
            except Exception as e:
                logger.error(CustomException(e))
                texts.append("")  # Append an empty string on error
                
        return "\n".join(texts)