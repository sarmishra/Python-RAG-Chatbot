import streamlit as st
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import openai
import os


# Load environment variables. Assumes that project contains .env file with API keys
load_dotenv()
#---- Set OpenAI API key 
# Change environment variable name from "OPENAI_API_KEY" to the name given in 
# your .env file.
openai.api_key = os.environ['OPENAI_API_KEY']

# Constants
CHROMA_PATH = "chroma"
PROMPT_TEMPLATE = """
Answer the question based only on the following context:

{context}

---

Answer the question based on the above context: {question}
"""

# Initialize once per session
@st.cache_resource
def load_db():
    embeddings = OpenAIEmbeddings()
    return Chroma(persist_directory=CHROMA_PATH, embedding_function=embeddings)

db = load_db()
llm = ChatOpenAI()

# Streamlit UI
st.set_page_config(page_title="Doc Q&A with RAG", layout="centered")
st.title("📘 Chat with Your Documents")

query_text = st.text_input("Enter your question:", placeholder="e.g., How does Alice meet the Mad Hatter?")
submit = st.button("Ask")

if submit and query_text:
    with st.spinner("Searching and thinking..."):
        results = db.similarity_search_with_relevance_scores(query_text, k=3)

        if len(results) == 0 or results[0][1] < 0.7:
            st.error("⚠️ Unable to find matching results.")
        else:
            # Build the prompt
            context_text = "\n\n---\n\n".join([doc.page_content for doc, _ in results])
            prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
            prompt = prompt_template.format(context=context_text, question=query_text)

            # Get model response
            response_text = llm.predict(prompt)
            sources = [doc.metadata.get("source", "Unknown") for doc, _ in results]

            # Display results
            st.markdown("### 💬 Response:")
            st.write(response_text)

            st.markdown("### 📚 Sources:")
            for source in sources:
                st.markdown(f"- `{source}`")