# FastAPI 임포트
from fastapi import FastAPI

# FastAPI 인스턴스 생성
app = FastAPI()

@app.get('/')
async def root():
    return{'message':'Hello FastAPI'}

@app.get('/items/{item_id}')
async def read_item(item_id) :
    return {'item_id':item_id}

# 타입이 있는 매개변수
@app.get('/itemnum/{item_num}')
async def read_num(item_num: int):
    return {'item_num': item_num}

@app.get('/users/me')
async def read_user_me() :
    return {'user_id':'the current user'}

@app.get('/users/{user_id}')
async def read_user(user_id:str):
    return {'user_id':user_id}