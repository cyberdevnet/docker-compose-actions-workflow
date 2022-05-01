from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(debug=True)

origins = [
    "http://localhost:3000",
    "localhost:3000",
    "http://127.0.0.1:3000",
    "127.0.0.1:3000",
    "http://localhost",
    "http://127.0.0.1"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@ app.get("/", tags=["root"])
async def read_root() -> dict:
    return {"message": "Welcome to docker-compose-actions-workflow"}