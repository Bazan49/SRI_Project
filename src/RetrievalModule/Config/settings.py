from pydantic_settings import BaseSettings, SettingsConfigDict


class RetrievalSettings(BaseSettings):
    lmir_mu: float = 100.0  # Reducido de 1000 para mayor discriminación
    default_top_k: int = 10
    
    model_config = SettingsConfigDict(extra="ignore")
