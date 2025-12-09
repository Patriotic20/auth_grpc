from pydantic import BaseModel, Field, field_validator
from core.utils.normalize_str import normalize_str

class Pagination(BaseModel):
    page: int = Field(..., ge=1)
    limit: int = Field(..., ge=1)
    search: str | None = None
    
    def offset(self) -> int:
        return (self.page - 1) * self.limit
    
    @field_validator("search", mode="before")
    @classmethod
    def normalize(cls, text):
        if text is None:
            return None
        return normalize_str(text=text)
