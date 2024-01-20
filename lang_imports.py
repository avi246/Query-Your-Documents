import streamlit as st
from PyPDF2 import PdfReader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS

from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader, TextLoader

import os
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
from langchain.agents import Tool
from langchain.agents import AgentType
from langchain.agents import initialize_agent
from langchain.chat_models import ChatOpenAI

# Set OpenAI API key
os.environ["OPENAI_API_KEY"] = "" #insert your openai api key inside the quotation marks.