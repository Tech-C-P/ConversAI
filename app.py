# Import necessary libraries and modules
from src.pipelines.completePipeline import Pipeline
import gradio as gr

# Initialize global variables
chain = None  # Holds the current processing chain
pipeline = Pipeline()  # Instantiate the processing pipeline

def getTextResponse(text: str, inputQuery: str) -> str:
    """
    Generate a response based on the input text and query.

    Args:
        text (str): The input text to process.
        inputQuery (str): The question to be answered.

    Returns:
        str: The response generated from the input text.
    """
    global chain
    if chain is None:
        chain = pipeline.plainText(text=text)  # Create a new processing chain for plain text
    response = chain.invoke({"question": inputQuery})  # Process the query
    return response

def getSearchablePdfResponse(path: str, inputQuery: str) -> str:
    """
    Generate a response based on a searchable PDF and query.

    Args:
        path (str): Path to the searchable PDF.
        inputQuery (str): The question to be answered.

    Returns:
        str: The response generated from the searchable PDF.
    """
    global chain
    if chain is None:
        chain = pipeline.searchablePdf(path=path)  # Create a new processing chain for the PDF
    response = chain.invoke({"question": inputQuery})
    return response

def getScannablePdfResponse(path: str, inputQuery: str) -> str:
    """
    Generate a response based on a scannable PDF and query.

    Args:
        path (str): Path to the scannable PDF.
        inputQuery (str): The question to be answered.

    Returns:
        str: The response generated from the scannable PDF.
    """
    global chain
    if chain is None:
        chain = pipeline.scannablePdf(path=path)  # Create a new processing chain for the scannable PDF
    response = chain.invoke({"question": inputQuery})
    return response

def clearFunction() -> None:
    """Reset the processing chain to prepare for new queries."""
    global chain
    chain = None

# User interface for text input
with gr.Blocks() as textInterface:
    with gr.Row():
        inputText = gr.Textbox(
            label="Input Text",
            placeholder="Enter your text here"
        )
    with gr.Row():
        question = gr.Textbox(
            label="Question",
            placeholder="Enter your question here"
        )
        answer = gr.Textbox(
            label="Response",
            interactive=False  # Make the response field read-only
        )
    with gr.Row():
        submitButton = gr.Button(value="Submit", variant="primary")
        clearButton = gr.ClearButton(
            components=[inputText, question, answer],
            value="Clear",
            variant="secondary"
        )
    # Define actions for buttons
    submitButton.click(fn=getTextResponse, inputs=[inputText, question], outputs=[answer])
    clearButton.click(fn=clearFunction)

# User interface for searchable PDF input
with gr.Blocks() as searchablePdf:
    with gr.Row():
        inputFile = gr.File(
            file_types=[".pdf"],  # Restrict file types to PDFs
            file_count="single",   # Allow only one PDF file selection
            label="Select PDF"
        )
    with gr.Row():
        question = gr.Textbox(label="Question", placeholder="Enter your question here")
        answer = gr.Textbox(label="Response", interactive=False)
    with gr.Row():
        submitButton = gr.Button(value="Submit", variant="primary")
        clearButton = gr.ClearButton(
            components=[inputFile, question, answer],
            value="Clear",
            variant="secondary"
        )
    # Define actions for buttons
    submitButton.click(fn=getSearchablePdfResponse, inputs=[inputFile, question], outputs=[answer])
    clearButton.click(fn=clearFunction)

# User interface for scannable PDF input
with gr.Blocks() as scannablePdf:
    with gr.Row():
        inputFile = gr.File(file_types=[".pdf"], file_count="single", label="Select PDF")
    with gr.Row():
        question = gr.Textbox(label="Question", placeholder="Enter your question here")
        answer = gr.Textbox(label="Response", interactive=False)
    with gr.Row():
        submitButton = gr.Button(value="Submit", variant="primary")
        clearButton = gr.ClearButton(
            components=[inputFile, question, answer],
            value="Clear",
            variant="secondary"
        )
    # Define actions for buttons
    submitButton.click(fn=getScannablePdfResponse, inputs=[inputFile, question], outputs=[answer])
    clearButton.click(fn=clearFunction)

def getLinksButtonFn(baseUrl: str) -> tuple:
    """
    Fetch links from the specified base URL.

    Args:
        baseUrl (str): The base URL from which to fetch links.

    Returns:
        tuple: A tuple containing a CheckboxGroup of fetched links and two rows for the UI.
    """
    links = pipeline.webCrawler.getLinks(url=baseUrl)  # Fetch links using the web crawler
    checkboxes = gr.CheckboxGroup(choices=links, label="Fetched Links", visible=True)
    row2 = gr.Row(visible=True)
    row3 = gr.Row(visible=True)
    return checkboxes, row2, row3

def getWebsiteResponse(links: list[str], inputQuery: str) -> str:
    """
    Generate a response based on fetched website links and a query.

    Args:
        links (list[str]): List of links to process.
        inputQuery (str): The question to be answered.

    Returns:
        str: The response generated from the website links.
    """
    global chain
    if chain is None:
        chain = pipeline.webCrawl(urls=links)  # Create a new processing chain for web crawling
    response = chain.invoke({"question": inputQuery})
    return response

def clearWebsiteResponse() -> gr.CheckboxGroup:
    """Clear the website response and reset the checkboxes."""
    global chain
    chain = None  # Reset the chain
    checkboxes = gr.CheckboxGroup(choices=[], label="Fetched Links", visible=False)
    return checkboxes

# User interface for website crawling
with gr.Blocks() as websiteCrawler:
    with gr.Row():
        inputUrl = gr.Textbox(
            label="Base URL",
            placeholder="Enter the Base URL to fetch other links",
            scale=3
        )
        getLinksButton = gr.Button(value="Get Links", variant="primary", scale=1)
    checkboxes = gr.CheckboxGroup(choices=[], label="Fetched Links")
    with gr.Row(visible=False) as row2:
        question = gr.Textbox(label="Question", placeholder="Enter your question here")
        answer = gr.Textbox(label="Response", interactive=False)
    with gr.Row(visible=False) as row3:
        submitButton = gr.Button(value="Submit", variant="primary")
        clearButton = gr.ClearButton(
            components=[question, answer],
            value="Clear",
            variant="secondary"
        )
    # Define actions for buttons
    getLinksButton.click(fn=getLinksButtonFn, inputs=[inputUrl], outputs=[checkboxes, row2, row3])
    submitButton.click(fn=getWebsiteResponse, inputs=[checkboxes, question], outputs=[answer])
    clearButton.click(fn=clearWebsiteResponse, inputs=None, outputs=[checkboxes])

def getYoutubeResponse(links: str, inputQuery: str) -> str:
    """
    Generate a response based on YouTube video links and a query.

    Args:
        links (str): Comma-separated YouTube video links.
        inputQuery (str): The question to be answered.

    Returns:
        str: The response generated from the YouTube videos.
    """
    global chain
    links = [link.strip() for link in links.split(",")]  # Split and clean the links
    if chain is None:
        chain = pipeline.youtubeLinks(urls=links)  # Create a new processing chain for YouTube links
    response = chain.invoke({"question": inputQuery})
    return response

# User interface for YouTube links
with gr.Blocks() as youtubeInterface:
    with gr.Row():
        inputLinks = gr.Textbox(
            label="Youtube Links",
            placeholder='Enter comma(,)-separated youtube video links'
        )
    with gr.Row():
        question = gr.Textbox(label="Question", placeholder="Enter your question here")
        answer = gr.Textbox(label="Response", interactive=False)
    with gr.Row():
        submitButton = gr.Button(value="Submit", variant="primary")
        clearButton = gr.ClearButton(
            components=[inputLinks, question, answer],
            value="Clear",
            variant="secondary"
        )
    # Define actions for buttons
    submitButton.click(fn=getYoutubeResponse, inputs=[inputLinks, question], outputs=[answer])
    clearButton.click(fn=clearFunction)

# Create a tabbed interface for the different functionalities
application = gr.TabbedInterface(
    [textInterface, searchablePdf, scannablePdf, websiteCrawler, youtubeInterface],
    ["Text", "Searchable PDF", "Scannable PDF", "Website Text", "Youtube Transcripts"]
)

# Launch the Gradio application
application.launch()