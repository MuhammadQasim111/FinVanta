from llama_index import VectorStoreIndex, ServiceContext, StorageContext
from llama_index.llms import OpenAI
from llama_index.vector_stores import FaissVectorStore
import faiss
import os

def create_vector_index(documents):
    d = 1536  # embedding dimension
    llm = OpenAI(api_key=os.getenv("GROK_API_KEY"))
    faiss_index = faiss.IndexFlatL2(d)
    vector_store = FaissVectorStore(faiss_index=faiss_index)
    storage_context = StorageContext.from_defaults(vector_store=vector_store)
    service_context = ServiceContext.from_defaults(llm=llm)
    index = VectorStoreIndex.from_documents(documents,
                                            service_context=service_context,
                                            storage_context=storage_context)
    return index
