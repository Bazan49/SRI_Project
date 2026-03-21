import chromadb
import numpy as np
from typing import List, Dict, Any, Optional
from EmbbedingsModule.Domain.vector_store import BaseVectorStore


class ChromaVectorStore(BaseVectorStore):
    """Adaptador Chroma para BaseVectorStore."""
    
    def __init__(self, collection_name: str, persist_path: str = "./chroma_db"):
        self.client = chromadb.PersistentClient(path=persist_path)
        self.collection = self.client.get_or_create_collection(name=collection_name)
    
    def add(
        self,
        ids: List[str],
        embeddings: np.ndarray,
        documents: List[str],
        metadata: List[Dict[str, Any]]
    ) -> None:
        self.collection.add(
            ids=ids,
            embeddings=embeddings.tolist(),
            documents=documents,
            metadatas=metadata
        )
    
    def search(self, query_vector: np.ndarray, k: int = 10, filters: Optional[Dict[str, Any]] = None) -> Dict[str, List[Any]]:
        
        if query_vector.ndim == 1:
            query_embeddings = [query_vector.tolist()]
        else:
            query_embeddings = query_vector.tolist()

        result = self.collection.query(
            query_embeddings=query_embeddings,
            n_results=k,
            where=filters,
            include=["documents", "metadatas", "distances", "embeddings"]
        )

        if not result or not result.get("ids"):
            return {"ids": [], "documents": [], "metadatas": [], "distances": [], "embeddings": []}

        return {
            "ids": result["ids"][0],
            "documents": result["documents"][0],
            "metadatas": result["metadatas"][0],
            "distances": result["distances"][0],
            "embeddings": result.get("embeddings", [[]])[0],
        }

    def delete(self, ids: List[str]) -> None:
        self.collection.delete(ids=ids)
    
    def update(
        self,
        ids: List[str],
        embeddings: Optional[np.ndarray] = None,
        documents: Optional[List[str]] = None,
        metadata: Optional[List[Dict[str, Any]]] = None
    ) -> None:
        # Chroma update requiere especificar qué actualizar
        update_data = {}
        if embeddings is not None:
            update_data["embeddings"] = embeddings.tolist()
        if documents is not None:
            update_data["documents"] = documents
        if metadata is not None:
            update_data["metadatas"] = metadata
        
        self.collection.update(ids=ids, **update_data)
    
