from fastapi import FastAPI

app = FastAPI()

# 쿼리 매개변수
# 경로 매개변수의 일부가 아닌 다른 함수 매개변수를 선언하면 "쿼리" 매개변수로 자동 해석

# 가상의 아이템 데이터베이스
items_db = [
    {'item_name':'Foo'},
    {'item_name':'Bar'},
    {'item_name':'Baz'}
]

@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    '''
    skip: int = 0: 건너뛸 아이템 개수 (기본값 0)
    limit: int = 10: 반환할 최대 아이템 개수 (기본값 10)
    이 매개변수들은 쿼리 매개변수로 작동합니다.
    '''
    return items_db[skip : skip + limit]