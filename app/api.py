from fastapi import APIRouter
from pydantic import BaseModel
from app.services import generate_sql
from app.models import QueryRequest, QueryResponse

router = APIRouter()


@router.post("/generate-sql",response_model=QueryResponse)
def generate_sql_query(req: QueryRequest):
    sql_query = generate_sql(req.prompt)
    return {"sql": generate_sql(req.prompt)}
