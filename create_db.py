from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
import chromadb

DATA_PATH = r"./data/"
CHROMA_PATH = r"chroma_db"
EMBEDDING_MODEL = "mxbai-embed-large:latest"

chroma_client = chromadb.PersistentClient(path=CHROMA_PATH)
embedding = OllamaEmbeddings(model=EMBEDDING_MODEL)
collection = chroma_client.get_or_create_collection(name="rag_data")

loader = PyPDFDirectoryLoader(DATA_PATH, glob="*.pdf")

raw_documents = loader.load()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=200,
    length_function=len,
    is_separator_regex=False,
    )

print(f"Loaded {len(raw_documents)} documents from {DATA_PATH}")

chunks = text_splitter.split_documents(raw_documents)

documents = []
metadata = []
ids = []

i = 0

for chunk in chunks:
    documents.append(chunk.page_content)
    metadata.append(chunk.metadata)
    ids.append("ID"+str(i))
    i += 1

vectors = embedding.embed_documents(documents)

collection.upsert(
    documents=documents,
    metadatas=metadata,
    ids=ids,
    embeddings=vectors,
)