import os

from langchain_core.documents import Document

# from llama_index import download_loader
from langchain_community.document_loaders import PreprocessLoader

API_KEY = (
    ""  # you've to contact support@preprocess.co for generating an api key for you...
)

def test_preprocess_load_document():
    filepath = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "preprocess_test.pdf"
    )
    loader = PreprocessLoader(api_key=API_KEY, filepath=filepath)
    documents = loader.load()

    assert isinstance(documents, list)
    assert all(isinstance(doc, Document) for doc in documents)
    assert all(doc.text is not None for doc in documents)