from pydantic_settings import BaseSettings, SettingsConfigDict






class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env",extra="ignore")


    GOOGLE_API_KEY:str
    LLM_MODEL:str = "gemini-2.5-flash"
    EMBEDDING_MODEL:str = "models/gemini-embedding-001"

config = Settings()