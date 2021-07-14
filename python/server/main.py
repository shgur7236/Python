#POST: 데이터를 생성하기 위해.
#GET: 데이터를 읽기 위해.
#PUT: 데이터를 업데이트하기 위해.
#DELETE: 데이터를 삭제하기 위해.

from fastapi import FastAPI

app = FastAPI()

@app.get('/users/me')
async def read_user_me():
    return {"user_id":"the current user"}

@app.get('/users/{user_id}')
async def read_user(user_id: str):
    return {"user_id": user_id}



