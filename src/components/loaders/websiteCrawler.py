from concurrent.futures import ThreadPoolExecutor
from src.utils.exceptions import CustomException
from urllib.parse import urlparse, urljoin
from src.utils.functions import getConfig, cleanText
from src.utils.logging import logger
from bs4 import BeautifulSoup
import time
import requests

class WebsiteCrawler:
    def __init__(self):
        """Initialize the WebsiteCrawler with configuration settings."""
        self.config = getConfig(path="config.ini")

    def getLinksFromPage(self, url: str) -> list[str]:
        """
        Extract all valid links from a given webpage.

        Args:
            url (str): The URL of the webpage to extract links from.

        Returns:
            list[str]: A list of extracted links from the page.
        """
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        anchors = soup.find_all("a")
        links = []

        for anchor in anchors:
            if "href" in anchor.attrs:
                if urlparse(anchor.attrs["href"]).netloc == urlparse(url).netloc:
                    links.append(anchor.attrs["href"])
                elif not anchor.attrs["href"].startswith(("//", "file", "javascript", "tel", "mailto", "http")):
                    links.append(urljoin(url + "/", anchor.attrs["href"]))
                
                links = [link for link in links if "#" not in link]
                links = list(set(links))

        return links

    def getLinks(self, url: str) -> list[str]:
        """
        Fetch and return all unique links found from the given URL.

        Args:
            url (str): The starting URL to fetch links from.

        Returns:
            list[str]: A list of unique links found.
        """
        try:
            logger.info("Fetching links from URL")
            start = time.time()
            links = self.getLinksFromPage(url)
            uniqueLinks = set()

            for link in links:
                now = time.time()
                if now - start > self.config.getint("WEBCRAWLER", "timeout"):
                    break
                uniqueLinks = uniqueLinks.union(set(self.getLinksFromPage(link)))

            return list(set([x[:-1] if x[-1] == "/" else x for x in uniqueLinks]))
        except Exception as e:
            logger.error(CustomException(e))

    def extractTextFromUrl(self, url: str) -> str:
        """
        Extract and clean text content from a given URL.

        Args:
            url (str): The URL of the webpage to extract text from.

        Returns:
            str: Cleaned text extracted from the webpage.
        """
        response = requests.get(url)
        response.raise_for_status()
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        return cleanText(text=soup.get_text(separator=' ', strip=True))

    def extractTextFromUrlList(self, urls: list[str]) -> str:
        """
        Extract text from a list of URLs concurrently.

        Args:
            urls (list[str]): A list of URLs to extract text from.

        Returns:
            str: All extracted text combined into a single string.
        """
        try:
            logger.info("Extracting text from URLs")
            with ThreadPoolExecutor() as executor:
                texts = list(executor.map(self.extractTextFromUrl, urls))
            return "\n".join(texts)
        except Exception as e:
            logger.error(CustomException(e))