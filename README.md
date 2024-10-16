# 🤖📚 ConversAI 

**[ConversAI](https://convers-ai-test.vercel.app/)** is an innovative conversational AI framework designed to empower users with intelligent interactions
across various document formats and web content. Utilizing advanced natural language processing (NLP) techniques,
ConversAI enables seamless text extraction and querying capabilities, making it an invaluable tool for researchers,
students, professionals, and anyone who regularly interacts with text-based information.

## Explore Our Chatbot Solutions

For advanced, tailored chatbot solutions, please visit [ConversAI Website](https://convers-ai-test.vercel.app/).
We offer a unique and customizable chatbot solution tailored to meet your specific needs. If you’re interested in enhancing your customer engagement with our chatbot technology, please reach out to us via email or visit our website for more information.
### Demo Video


## 📖 Introduction 

In an era characterized by information overload, efficient data processing is crucial. ConversAI addresses this
challenge by leveraging state-of-the-art technologies to transform unstructured data into actionable insights. Whether
extracting meaningful information from PDFs, fetching transcripts from YouTube videos, or gathering data from multiple
web pages, ConversAI provides a user-friendly interface that simplifies these complex tasks.

## 🏗️ Architecture Overview

![PDF Upload](demo/conversai-architecture-diagram.png)

### Key Technologies Used:

- **Gradio**: For building the interactive user interface.
- **Langchain**: For chaining various data retrieval and processing tasks.
- **EasyOCR**: For optical character recognition in scannable PDFs.
- **Pymupdf**: For handling searchable PDF documents.
- **BeautifulSoup**: For web scraping and HTML parsing.

With its modular design, ConversAI is not just a tool but a platform that can be extended and customized to fit diverse
user requirements.

## ✨ Features

| Feature                      | Description                                                                 |
|------------------------------|-----------------------------------------------------------------------------|
| **Text Extraction**          | Extracts text from both searchable and scannable PDFs.                      |
| **Web Crawler**              | Gathers and processes text from websites efficiently.                       |
| **YouTube Transcript Retrieval** | Fetches and processes video transcripts for easy querying.                |
| **Conversational Interface** | Interactive Gradio UI for seamless user interaction.                       |
| **Configurable**             | Easily customizable to fit specific use cases.                              |
| **Advanced Document Retrieval** | Utilizes sophisticated algorithms for improved accuracy and relevance.     |
## 🌟 Benefits

- **Time-Saving**: Automates text extraction, allowing users to focus on analysis rather than manual data entry.
- **Accuracy**: High-precision text extraction capabilities ensure that users receive reliable data.
- **User-Friendly**: Intuitive interface makes it accessible for users with varying technical skills.
- **Scalable**: Modular architecture allows for easy integration of additional features and functionalities.

## 🚀 Getting Started

### 🗂️ Prerequisites

Before running ConversAI, ensure you have the following dependencies installed:

```bash
apt-get update && apt-get upgrade -y
apt-get install poppler-utils -y
```

Additionally, you need to set up your environment variables for the GROQ API:

1. Sign up on [Groq](https://www.groq.com) and obtain your API key.
2. Set the `GROQ_API_KEY` in your environment variables.

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/rauhanahmed/ConversAI.git
   cd ConversAI
   ```

2. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

To launch the application, run the following command:

```bash
python app.py
```

The Gradio interface will open in your default web browser.

### Important Configuration Note

In case a GPU is unavailable, please modify the `config.ini` file as follows:

- Under the `[EMBEDDINGS]` section, change:
  ```ini
  device = cuda
  ```
  to:
  ```ini
  device = cpu
  ```

- Under the `[EASYOCR]` section, change:
  ```ini
  gpu = true
  ```
  to:
  ```ini
  gpu = false
  ```

These adjustments will ensure that the application runs smoothly on CPU resources.

###  📝 Important Note 

After using the interface, be sure to click the "Clear" button to reset the fields. This is crucial because session
management has not been implemented in this version, and failing to clear inputs may lead to unintended data persistence
during subsequent interactions.

## 🗂️ Directory Structure

Here's a comprehensive view of the project's directory tree:

```
ConversAI/
├── app.py                      # Main application file
├── requirements.txt            # Required Python packages
├── src/                        # Source code directory
│   ├── components/             # Component modules
│   │   ├── loaders/            # Data loaders
│   │   │   ├── pdfLoader.py
│   │   │   ├── websiteCrawler.py
│   │   │   └── youtubeLoader.py
│   │   ├── rag/                # Retrieval-Augmented Generation components
│   │   │   └── RAG.py
│   │   ├── utils/              # Utility functions and classes
│   │   │   ├── functions.py
│   │   │   ├── exceptions.py
│   │   │   └── logging.py
│   │   └── vectors/            # Vector storage and processing
│   │       └── vectorstore.py
│   ├── pipelines/              # Pipeline logic for data processing
│   │   └── completePipeline.py
│   └── settings/               # Configuration files
│       ├── config.ini
│       └── params.yaml
└── README.md                   # Project documentation
```

## 🎥 Demo

### Text Input Interface

![Text Input](demo/TextInterface.png)

### PDF Upload Interface

![PDF Upload](demo/PDFInterface.png)

### Web Crawler Interface

![Web Crawler](demo/WebsiteInterface.png)

## 📝 Conclusion

ConversAI is more than just a tool; it’s a comprehensive solution for managing and extracting insights from a multitude
of document formats and web sources. With its powerful capabilities and user-friendly interface, ConversAI is poised to
make information retrieval and processing easier and more efficient than ever before.

Sure! Here’s an updated section to include your contributions and acknowledgments:

---

## 👤 Author Information

| Author           | 📧 Email                            | 💻 GitHub                                       | 🔗 LinkedIn                                           | 🐦 Twitter                                        | 🌐 Portfolio                                |
|------------------|-------------------------------------|-------------------------------------------------|-------------------------------------------------------|--------------------------------------------------|---------------------------------------------|
| **Rauhan Ahmed** | rauhaan.siddiqui@gmail.com          | [RauhanAhmed](https://github.com/RauhanAhmed)    | [Rauhan Ahmed](https://www.linkedin.com/in/rauhan-ahmed) | [@ahmed_rauh46040](https://x.com/ahmed_rauh46040) | [rauhanahmed.org](https://rauhanahmed.org)  |
| **Ishwor Subedi**| ishwor.subedi@email.com             | [IshworSubedi](https://github.com/ishworrsubedii)  | [Ishwor Subedi](https://www.linkedin.com/in/ishworrsubedii) | [@ishwor_subedi](https://x.com/ishworr_) | [ishworsubedi.com](https://ishwor-subedi.com.np) |
| **Faham**        | faham@email.com                     | [Faham](https://github.com/iamfaham)                | [Faham](https://www.linkedin.com/in/iamfaham)             | [@faham_twitter](https://x.com/iamfaham)  | [faham.com](https://iamfaham.netlify.app)             |

## 🙏 Acknowledgments 

This project was developed while working as an AI Engineer
at [Tech Consulting Partners](https://www.techconsultingpartners.com). I built ConversAI from scratch, implementing
advanced document retrieval methods, reranking techniques, hybrid search methodologies, multiple integrations with large
language models (LLMs), and lots of other complex functionalities.

The backend includes user management features, sophisticated data storage solutions (including S3 storage management),
database management, and vector databases. The deployment strategy leverages robust APIs, Docker containers, CI/CD
practices, model monitoring, and cloud platform deployment.

This open-source prototype serves as a stepping stone towards a more comprehensive project aimed at public good,
showcasing the immense potential of advanced AI technologies in everyday applications. I extend my heartfelt gratitude
to Tech Consulting Partners for entrusting me with this initiative and for their invaluable support throughout the
development process.

## 📜 License 

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

We hope you enjoy using ConversAI! For any questions or feedback, please reach out via the project repository or email.