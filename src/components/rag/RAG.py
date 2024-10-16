from src.components.vectors.vectorstore import VectorStore
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableLambda
from src.utils.exceptions import CustomException
from src.utils.functions import getConfig, loadYaml
from src.utils.logging import logger
from langchain_groq import ChatGroq

class Chain:
    def __init__(self):
        """Initialize the Chain with configuration and prompt template."""
        self.config = getConfig(path="config.ini")
        self.store = VectorStore()
        prompt = loadYaml(path="params.yaml")["prompt"]
        self.prompt = ChatPromptTemplate.from_template(prompt)

    def formatDocs(self, docs) -> str:
        """
        Format a list of documents into a single string.

        Args:
            docs: A list of documents to format.

        Returns:
            str: Formatted string with documents or a placeholder if empty.
        """
        context = ""
        for doc in docs:
            context += f"{doc}\n\n\n"
        if context == "":
            context = "No Context Found"
        else:
            pass
        return context

    def returnChain(self, text: str):
        """
        Create and return a processing chain based on the input text.

        Args:
            text (str): Input text to prepare the chain.

        Returns:
            Chain: Configured chain for processing input.
        """
        try:
            logger.info("Preparing chain")
            store = self.store.setupStore(text=text)
            chain = (
                {"context": RunnableLambda(lambda x: x["question"]) | store | RunnableLambda(self.formatDocs),
                 "question": RunnableLambda(lambda x: x["question"])}
                | self.prompt
                | ChatGroq(model_name=self.config.get("LLM", "llmModel"),
                           temperature=self.config.getfloat("LLM", "temperature"),
                           max_tokens=self.config.getint("LLM", "maxTokens"))
                | StrOutputParser()
            )
            return chain
        except Exception as e:
            logger.error(CustomException(e))