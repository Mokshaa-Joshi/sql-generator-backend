from fastapi import APIRouter
from pydantic import BaseModel
from app.services import generate_sql

router = APIRouter()

class QueryRequest(BaseModel):
    prompt: str

@router.post("/generate-sql")
def generate_sql_query(req: QueryRequest):
    return {"sql": generate_sql(req.prompt)}
