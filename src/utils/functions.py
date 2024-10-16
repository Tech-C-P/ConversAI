import configparser
import string
import yaml

def getConfig(path: str):
    """
    Load configuration from a specified file.

    Args:
        path (str): The path to the configuration file.

    Returns:
        ConfigParser: The loaded configuration object.
    """
    config = configparser.ConfigParser()
    config.read(path)
    return config

def cleanText(text: str):
    """
    Clean the input text by removing newline characters and punctuation.

    Args:
        text (str): The text to be cleaned.

    Returns:
        str: The cleaned text.
    """
    text = text.replace("\n", " ")
    text = text.translate(str.maketrans('', '', string.punctuation.replace(".", "")))
    return text

def loadYaml(path: str):
    """
    Load YAML content from a specified file.

    Args:
        path (str): The path to the YAML file.

    Returns:
        dict: The parsed content of the YAML file.
    """
    with open(path) as file:
        return yaml.safe_load(file)