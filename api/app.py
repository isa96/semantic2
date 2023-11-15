from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create boilerplate response
boilerplate_response = {
    "status_code" : 200, 
    "message" : "Success", 
    "data" : []
}

@app.get("/")
async def root():
    return boilerplate_response

@app.get("/query/{input_query}")
async def get_similar_query(input_query: str):
    similar_query = input_query + "(Similar)"
    boilerplate_response["data"] = [similar_query]
    return boilerplate_response