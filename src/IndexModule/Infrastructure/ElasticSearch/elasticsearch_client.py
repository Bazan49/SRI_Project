from elasticsearch import Elasticsearch, AsyncElasticsearch
from typing import Optional

class ElasticsearchClient:
    def __init__(
        self,
        hosts: list[str],
        username: str,
        password: str,
        verify_certs: bool = False
    ):
        self.sync_client = Elasticsearch(
            hosts=hosts,
            basic_auth=(username, password),
            verify_certs=verify_certs,
            request_timeout=30
        )
        self.async_client = AsyncElasticsearch(
            hosts=hosts,
            basic_auth=(username, password),
            verify_certs=verify_certs,
            request_timeout=30
        )
    
    def get_sync(self) -> Elasticsearch:
        return self.sync_client
    
    async def get_async(self) -> AsyncElasticsearch:
        return self.async_client
