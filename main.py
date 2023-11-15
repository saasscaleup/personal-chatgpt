from fastapi import FastAPI, HTTPException
from GodChatGPT import GodChatGPT
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app = FastAPI()
god_chatgpt = GodChatGPT()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"Hello":"ScaleUp SaaS"}

@app.get("/god-chatgpt")
def run_god_chatgpt(query: str):
    result = god_chatgpt.agent_executor({"input": query})
    print(result)
    return {"result":result['output']}
