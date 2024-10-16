from setuptools import setup, find_packages

HYPEN_E_DOT = "-e ."

def getRequirements(requirementsPath: str) -> list[str]:
    with open(requirementsPath) as file:
        requirements = file.read().split("\n")
    requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name="ConversAI",
    author="Rauhan Ahmed Siddiqui",
    author_email="rauhaan.siddiqui@gmail.com",
    version="0.1",
    packages=find_packages(),
    install_requires=getRequirements(requirementsPath="requirements.txt"),
    description="ConversAI: An innovative conversational AI framework for intelligent text extraction and querying.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
)
