# FastAPI 임포트
from fastapi import FastAPI

# FastAPI 인스턴스 생성
app = FastAPI()

@app.get('/')
async def root():
    return{'message':'Hello FastAPI'}