from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    elasticsearch_hosts: list[str] = ["https://localhost:9200"]
    elasticsearch_username: str = "elastic"
    elasticsearch_password: str = "TU_PASSWORD"
    index_name: str = "scraped-docs"

    class Config:
        env_file = ".env"
