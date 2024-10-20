from fastapi import FastAPI, Query, Path, HTTPException
import uvicorn

from typing import Optional, Annotated, List

from pydantic import BaseModel, Field

class Passport(BaseModel): # Модель json данных
    serial_num : Annotated[int, Field(ge=0)] = 69
    num : int = 12

class User(BaseModel): # Модель json данных
    name : str
    age : int = 18
    passport : Passport

    model_config = {  # Чисто пример конфига для сваггера, не связан никак с моделью
        "json_schema_extra": {
            "examples": [
                {
                    "name": "gleb",
                    "price": 12.5,
                    "tax": 200
                }
            ]
        }
    }

app = FastAPI()

@app.post("/hello/{name}", status_code=201)
async def hello(
    name: str,  # параметр урла
    user: User, # Модель JSON
    query_par: Annotated[int, Query(description='test query', ge=10)] = None, # Параметр query, которые в урле после ? идет
) -> str:
    if user.age < 18:
        # Чисто показать работу с ошибкой и ее статус кодом
        raise HTTPException(status_code=404, detail="Too young") 
    return 'ok'

if __name__=="__main__":
    uvicorn.run("app:app", reload=True)