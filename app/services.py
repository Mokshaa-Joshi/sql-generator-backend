import os
import pinecone
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer
from huggingface_hub import InferenceClient, login

load_dotenv()
pinecone_api_key = os.getenv("PINECONE_API_KEY")
hf_token = os.getenv("HUGGINGFACE_TOKEN")

# Login to HuggingFace
login(hf_token)
client = InferenceClient(model="mistralai/Mixtral-8x7B-Instruct-v0.1", token=hf_token)

# Pinecone
pc = pinecone.Pinecone(api_key=pinecone_api_key)
index = pc.Index("text-sql")

embed_model = SentenceTransformer('thenlper/gte-small')

def generate_sql(user_input: str) -> str:
    query_embedding = embed_model.encode(user_input).tolist()
    context = ""
    try:
        results = index.query(vector=query_embedding, top_k=3, include_metadata=True)
        if results.matches:
            for match in results.matches:
                metadata = match.metadata
                table_name = metadata.get("table_name", "")
                columns = metadata.get("columns", "")
                context += f"Table: {table_name}\nColumns: {columns}\n\n"
    except Exception as e:
        context = ""

    prompt = f"""You are a helpful SQL assistant.
Given the context:\n{context}
And the following user request:\n{user_input}
Write a full SQL query for this request.
Respond with only the SQL query.
"""
    response = client.text_generation(
        prompt=prompt,
        max_new_tokens=300,
        temperature=0.2,
        top_p=0.95,
        repetition_penalty=1.1,
    )
    return response.strip()
