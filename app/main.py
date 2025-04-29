from fastapi import FastAPI
from app.api import router

app = FastAPI(title="SQL Generator API")
app.include_router(router)
