# RAG Base - PDF Document Q&A System

A simple yet powerful Retrieval-Augmented Generation (RAG) system built with Ollama, ChromaDB, and LangChain. This project enables you to query PDF documents using natural language questions.

## 🚀 Features

- **PDF Document Processing**: Automatically loads and processes PDF files from a directory
- **Vector Embeddings**: Uses Ollama's `mxbai-embed-large` model for generating embeddings
- **Vector Database**: Stores embeddings in ChromaDB for efficient similarity search
- **Interactive Q&A**: Chat interface to ask questions about your documents
- **Context-Aware Responses**: LLM (Qwen3:1.7b) provides answers based on retrieved document context

## 📋 Prerequisites

- Python 3.12 or higher
- [Ollama](https://ollama.ai/) installed and running
- Required Ollama models:
  - `mxbai-embed-large:latest` (for embeddings)
  - `qwen3:1.7b` (for LLM)

## 🛠️ Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd rag-base
```

2. Install dependencies using `uv` (recommended) or `pip`:

```bash
# Using uv
uv sync

# Or using pip
pip install -r requirements.txt
```

3. Install required Ollama models:

```bash
ollama pull mxbai-embed-large:latest
ollama pull qwen3:1.7b
```

## 📁 Project Structure

```
rag-base/
├── data/              # Place your PDF files here
├── chroma_db/         # ChromaDB vector database (auto-generated)
├── create_db.py       # Script to create and populate the vector database
├── main.py            # Main Q&A application
├── pyproject.toml     # Project dependencies
└── README.md          # This file
```

## 🚀 Usage

### Step 1: Prepare Your Documents

Place your PDF files in the `data/` directory:

```bash
cp your-documents.pdf data/
```

### Step 2: Create the Vector Database

Run the database creation script to process PDFs and create embeddings:

```bash
python create_db.py
```

This script will:

- Load all PDF files from the `data/` directory
- Split documents into chunks (300 chars with 200 char overlap)
- Generate embeddings using Ollama
- Store everything in ChromaDB

### Step 3: Start the Q&A Interface

Run the main application:

```bash
python main.py
```

You'll be prompted to ask questions about your documents. Type your question and press Enter. To exit, press Enter with an empty query.

## ⚙️ Configuration

You can modify the following constants in the code:

- `DATA_DIR`: Directory containing PDF files (default: `"data"`)
- `CHROMA_DIR`: ChromaDB storage directory (default: `"chroma_db"`)
- `EMBEDDING_MODEL`: Ollama embedding model (default: `"mxbai-embed-large:latest"`)
- `LLM_MODEL`: Ollama LLM model (default: `"qwen3:1.7b"`)

### Text Chunking Parameters

In `create_db.py`, you can adjust:

- `chunk_size`: Size of text chunks (default: 300)
- `chunk_overlap`: Overlap between chunks (default: 200)

### Retrieval Parameters

In `main.py`, you can modify:

- `n_results`: Number of document chunks to retrieve (default: 3)

## 🔧 How It Works

1. **Document Processing** (`create_db.py`):

   - PDFs are loaded using LangChain's `PyPDFDirectoryLoader`
   - Documents are split into smaller chunks
   - Each chunk is embedded using Ollama embeddings
   - Embeddings are stored in ChromaDB with metadata

2. **Query Processing** (`main.py`):
   - User query is embedded using the same embedding model
   - Similar chunks are retrieved from ChromaDB
   - Retrieved context is passed to the LLM
   - LLM generates an answer based on the context

## 📦 Dependencies

- `langchain`: Core LangChain framework
- `langchain-community`: Community integrations
- `langchain-ollama`: Ollama integration
- `langchain-text-splitters`: Text splitting utilities
- `chromadb`: Vector database
- `pypdf`: PDF processing

## 📝 License

This project is open source and available under the MIT License.

---

**Note**: Make sure Ollama is running before executing the scripts. The system will use local models, so no API keys are required!
