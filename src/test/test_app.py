import pytest
from httpx import AsyncClient
from app import *

@pytest.mark.anyio
async def test_root():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/")
        assert response.status_code == 200
        assert response.json() == {"message": "Welcome to docker-compose-actions-workflow"}
    

@pytest.mark.anyio
async def test_post():
    payload = {"message": "ciao"}
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/post", json=payload)
        print(response)
        assert response.status_code == 200
        assert response.json() == {"message": payload["message"]}
