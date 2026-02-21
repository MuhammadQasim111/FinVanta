# modules/vector_index.py
import faiss
from llama_index.core import VectorStoreIndex, StorageContext
from llama_index.vector_stores.faiss import FaissVectorStore  # âœ… correct subpackage path


def create_vector_index(documents):
    # Dimension must match your embedding model output
    # text-embedding-ada-002 (OpenAI default) = 1536
    # text-embedding-3-small = 1536
    d = 1536
    faiss_index = faiss.IndexFlatL2(d)

    vector_store = FaissVectorStore(faiss_index=faiss_index)
    storage_context = StorageContext.from_defaults(vector_store=vector_store)

    # ServiceContext is deprecated in v0.10+ â€” Settings object is used automatically
    index = VectorStoreIndex.from_documents(
        documents,
        storage_context=storage_context,
    )
    return index
