# PromptPal: A LangChain-Based Chatbot
## Introduction

PromptPal is a simple yet powerful chatbot implemented using LangChain. It leverages vector storage to provide efficient retrieval of documents, enhancing the chatbot's ability to deliver accurate and contextually relevant responses.

## Repository Structure

- **app**: For streamlit app.
- **chat**: Chatting functionality .
- **utils**: utility functions.
## Features

- **Document Loader**: Efficiently loads and processes documents.
- **Vector Store**: Stores documents in a vectorized format for fast retrieval.
- **LangChain Chatbot**: Utilizes LangChain to set up a chatbot with advanced retrieval capabilities.

## Requirements

- Python 3.x
- LangChain
- NumPy
- Scikit-learn
- Faiss (for vector storage)
- Streamlit 

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/skp-github/PromptPal.git
    cd PromptPal
    ```

2. Create a virtual environment and activate it:
    ```bash
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
  ```bash
    streamlit run app.py
  ```
