# modules/vector_index.py
from llama_index import VectorStoreIndex, ServiceContext, StorageContext
from llama_index.vector_stores import FaissVectorStore
import faiss

def create_vector_index(documents):
    # Create FAISS index
    d = 1536  # adjust based on embedding dimension
    faiss_index = faiss.IndexFlatL2(d)
    vector_store = FaissVectorStore(faiss_index=faiss_index)

    storage_context = StorageContext.from_defaults(vector_store=vector_store)
    service_context = ServiceContext.from_defaults()

    index = VectorStoreIndex.from_documents(
        documents,
        service_context=service_context,
        storage_context=storage_context
    )
    return index
