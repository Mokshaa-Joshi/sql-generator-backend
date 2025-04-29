import os
from dotenv import load_dotenv

def load_env_variables():
    load_dotenv()
    huggingface_api_key = os.getenv("HUGGINGFACE_TOKEN")
    pinecone_api_key = os.getenv("PINECONE_API_KEY")
    return huggingface_api_key, pinecone_api_key

def build_prompt(context: str, user_input: str) -> str:
    prompt = f"""You are a helpful SQL assistant.
Given the context:\n{context}
And the following user request:\n{user_input}
Write a full SQL query for this request.
Respond with only the SQL query.
"""
    return prompt
