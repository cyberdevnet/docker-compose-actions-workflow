from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import motor.motor_asyncio
import os



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

FASTAPI_ENV_DEFAULT = 'production'
if os.getenv('FASTAPI_ENV',    FASTAPI_ENV_DEFAULT) == 'development':
    mongodb_url = "mongodb://localhost:27017/"
else:
    mongodb_url = "mongodb://mongodb:27017/"



# Initializing MONGODB DataBase
print("Environment is:", os.getenv('FASTAPI_ENV',    FASTAPI_ENV_DEFAULT))
try:
    MONGO_DETAILS = mongodb_url
    client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
    
    database = client.actionworkflowDB
    print("[+] Database connected to", mongodb_url)
    players = database.get_collection("players")

    # returned = actionworkflow_collection.find_one()
    # print(returned)
    test_collection = {'name': 'Mario','surname': 'Götze','position': 'striker'}
    players.replace_one({'name': 'Mario','surname': 'Götze','position': 'striker'},test_collection, upsert=True)

except Exception as error:
    print('DB error: ', error)
    print("[+] Database connection error!")
    print('mongodb_url: ', mongodb_url)



class postData(BaseModel):
    message: str


@ app.get("/", tags=["root"])
async def read_root() -> dict:
    return {"message": "Welcome to docker-compose-actions-workflow"}


@ app.post("/post", tags=["post"])
async def add_post(data: postData):
    message = data.message
    return {"message": message}