from langchain_chroma import Chroma
from openai.resources.vector_stores.vector_stores import VectorStoresWithStreamingResponse
import config_data as config
import os
from dotenv import load_dotenv

load_dotenv()

class VectorStores:
    
    def __init__(self,embedding):
        self.embedding = embedding

        self.vector_store = Chroma(
            collection_name=config.collection_name,
            embedding_function=self.embedding,
            persist_directory=config.persist_directory,
        )
    
    def get_retriever(self):
        return self.vector_store.as_retriever(search_kwargs={"k":config.similarity_threshold})

if __name__ == "__main__":
    from langchain_community.embeddings import DashScopeEmbeddings
    retriever=VectorStores(DashScopeEmbeddings(model=os.getenv("DASHSCOPE_EMBEDDING_MODEL"))).get_retriever()
    
    res = retriever.invoke("give me a Company Policy about remote work?")

    print(res)