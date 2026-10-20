from pydantic import field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore",
    )

    APP_NAME: str = "System Design Studio"
    APP_VERSION: str = "0.1.0"
    ENVIRONMENT: str = "development"
    DEBUG: bool = True
    PORT: int = 8000
    HOST: str = "0.0.0.0"

    # CORS
    ALLOWED_ORIGINS: list[str] | str = [
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ]

    @field_validator("ALLOWED_ORIGINS", mode="before")
    @classmethod
    def assemble_cors_origins(cls, v: str | list[str]) -> list[str]:
        if isinstance(v, str):
            if v.startswith("[") and v.endswith("]"):
                import json

                try:
                    return json.loads(v)
                except Exception:
                    pass
            return [i.strip() for i in v.split(",") if i.strip()]
        return v

    # Database
    DATABASE_URL: str = (
        "postgresql+asyncpg://postgres:postgres@localhost:5432/system_design_studio"
    )

    # Qdrant Vector DB
    QDRANT_URL: str = "http://localhost:6333"
    QDRANT_GRPC_PORT: int = 6334
    QDRANT_COLLECTION: str = "knowledge_chunks"
    QDRANT_LOCAL_PATH: str = "./qdrant_storage"

    # Embedding & Reranker
    EMBEDDING_PROVIDER: str = "fastembed"
    EMBEDDING_MODEL: str = "BAAI/bge-m3"
    SPARSE_EMBEDDING_MODEL: str = "Qdrant/bm25"
    RERANKER_ENABLED: bool = True
    RERANKER_MODEL: str = "BAAI/bge-reranker-v2-m3"

    # Data paths
    DATA_DIR: str = "./data"

    # LLM Settings (DeepSeek-R1-Distill-Qwen-32B)
    LLM_PROVIDER: str = "ollama"  # "ollama", "vllm", or "mock"
    LLM_MODEL: str = "deepseek-r1:32b"
    LLM_BASE_URL: str = "http://localhost:11434"
    LLM_API_KEY: str | None = None
    LLM_TEMPERATURE: float = 0.2
    LLM_MAX_RETRIES: int = 2
    LLM_HF_BUCKET: str = "keshavrao887/DeepSeek-R1-Distill-Qwen-32B-bucket"
    LLM_LOCAL_MODEL_PATH: str = "./models/DeepSeek-R1-Distill-Qwen-32B"

    # Logging
    LOG_LEVEL: str = "INFO"


settings = Settings()
