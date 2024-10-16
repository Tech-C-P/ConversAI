from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_community.docstore.document import Document
from langchain_huggingface import HuggingFaceEmbeddings
from src.utils.exceptions import CustomException
from src.utils.functions import getConfig
from src.utils.logging import logger

class VectorStore:
    def __init__(self):
        """Initialize the VectorStore with configuration, embeddings, and text splitter."""
        self.config = getConfig(path="config.ini")
        self.vectorEmbeddings = HuggingFaceEmbeddings(
            model_name=self.config.get("EMBEDDINGS", "embeddingModel"),
            model_kwargs={"device": self.config.get("EMBEDDINGS", "device")},
            encode_kwargs={"normalize_embeddings": self.config.getboolean("EMBEDDINGS", "normalize_embeddings")}
        )
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=self.config.getint("VECTORSTORE", "chunkSize"),
            chunk_overlap=self.config.getint("VECTORSTORE", "chunkOverlap"),
            add_start_index=self.config.getboolean("VECTORSTORE", "addStartIndex")
        )

    def setupStore(self, text: str):
        """
        Set up the vector store with the provided text.

        Args:
            text (str): The text to store and process.

        Returns:
            Retriever: A retriever for querying the vector store.
        """
        try:
            store = InMemoryVectorStore(self.vectorEmbeddings)
            textDocument = Document(page_content=text)
            documents = self.splitter.split_documents([textDocument])
            store.add_documents(documents=documents)
            return store.as_retriever(
                search_type=self.config.get("RETRIEVER", "searchType"),
                search_kwargs={
                    "k": self.config.getint("RETRIEVER", "k"),
                    "fetch_k": self.config.getint("RETRIEVER", "fetchK")
                }
            )
        except Exception as e:
            logger.error(CustomException(e))
            print(CustomException(e))