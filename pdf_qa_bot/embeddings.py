"""Utilities for creating embeddings and vector spaces"""

from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS


def text_splitter(raw_text: str):
    """text splitter"""

    text_splitter = CharacterTextSplitter(separator="\n", chunk_size=800,
                                          chunk_overalp=200, length_function=len)
    texts = text_splitter.split_text(raw_text)
    return texts


