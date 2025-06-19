# 🧠 RAG + LangChain: AI Chatbot for Docs

Build an AI-powered chatbot using **RAG (Retrieval-Augmented Generation)** with **Python**, **LangChain**, **ChromaDB**, and **OpenAI**. It allows you to ask questions about documents (such as PDFs, Markdown files, etc.) and receive context-aware, grounded responses with source citations.

---

## 🚀 Features

- Chat with your local files (Markdown, text, etc.)
- Uses RAG for more accurate, grounded answers
- Generate responses using OpenAI's GPT models
- Fast similarity search with ChromaDB
- Source chunk citation for transparency
- Run via command line or a clean Streamlit UI

---

## 🧰 Tech Stack

- **Python**
- **LangChain**
- **ChromaDB**
- **OpenAI (embeddings + LLM)**
- **Streamlit** (for web UI)

---

## 💻 Setup Instructions

### 1. Install Dependencies

1. Run this command to install dependenies in the `requirements.txt` file.

```python
pip install -r requirements.txt
```

2. Install markdown depenendies with:

```python
pip install "unstructured[md]"
```

### 2. Set Your OpenAI API Key

Create a .env file in the root directory and define your API Key's value there.

```.env
OPENAI_API_KEY=your_api_key_here
```

### 3. Create database

Create the Chroma DB.

```python
python create_database.py
```

---

## ▶️ Usage

### Option 1: Command Line Interface

Ask questions from terminal using:

```bash
python query_data.py "How does Alice meet the Mad Hatter?"
```

• Uses similarity search + relevance threshold (>= 0.7)
• Returns a formatted response and document sources

### Option 2: Option 2: Streamlit Web App

Launch the UI:

```bash
streamlit run app.py
```

Then open http://localhost:8501 in your browser.
• Enter a question in the input box
• See the AI response and source documents instantly

---

## 🛠️ How It Works

1. Load Documents: Preprocessed and stored in Chroma vector DB.
2. Chunking: Large texts are split into ~1000-character chunks.
3. Embedding: Uses OpenAI embeddings to convert text into vectors.
4. Search: Uses vector similarity to retrieve relevant chunks.
5. Prompting: Combines retrieved context and question into a prompt.
6. LLM Response: Uses OpenAI Chat API to generate grounded answers.

---

## How to create an OpenAI API Key

> Need to set up an OpenAI account and generate the OpenAI key from here : [Create a new secret key](https://platform.openai.com/api-keys). We will need to make a payment for the OpenAI API to work.

## 🖼️ Preview

![Landing Page](https://github.com/sarmishra/Python-RAG-Chatbot/blob/main/AI_Chatbot_UI.png)
