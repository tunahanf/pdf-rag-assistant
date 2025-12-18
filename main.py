import chromadb
from langchain_ollama import ChatOllama, OllamaEmbeddings

DATA_DIR = r"data"
CHROMA_DIR = r"chroma_db"
EMBEDDING_MODEL = "mxbai-embed-large:latest"

chroma_client = chromadb.PersistentClient(path=CHROMA_DIR)
collection = chroma_client.get_or_create_collection(name="rag_data")

embedding = OllamaEmbeddings(model=EMBEDDING_MODEL)

llm = ChatOllama(model="qwen3:1.7b", temperature=0.7)

while True:
    user_query = input("What do you want to know about monopoly: ").strip()
    if not user_query:
        print("Exiting the chat.")
        break
    q_vec = embedding.embed_query(user_query)
    results = collection.query(
        query_embeddings=[q_vec],
        n_results=3,
        include=["metadatas", "documents"]
    )
    docs = results['documents'][0]
    context = "\n\n---\n\n".join(docs)

    messages = [("system",
        "Sen bir RAG asistanısın. Sadece verilen CONTEXT'e dayanarak cevap ver. "
        "Context'te yoksa 'Bunu verilen dokümanlarda bulamadım' de."),
        ("user", f"CONTEXT:\n{context}\n\nSORU:\n{user_query}")
    ]
    answer = llm.invoke(messages)
    print(f"ANSWER: {answer.content}\n")