from pydantic import BaseModel

class QueryRequest(BaseModel):
    prompt: str

class QueryResponse(BaseModel):
    sql: str
