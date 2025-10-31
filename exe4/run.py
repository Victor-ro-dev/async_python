from sqlalchemy import MetaData, Table, Column, Integer, String
import databases
from fastapi import FastAPI
from fastapi.responses import JSONResponse
import uvicorn
import asyncio


DATABASE_URL = 'sqlite:///./schema.db'
database = databases.Database(DATABASE_URL)

metadata = MetaData()
PESSOA = Table(
    'person', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String)
)

async def get_all_people():
    query = PESSOA.select()
    result = await database.fetch_all(query)
    return result


app = FastAPI()

@app.get("/")
async def read_data():
    await database.connect()
    result = await get_all_people()
    print(result)

    formatted_result = []
    for row in result:
        formatted_result.append({"id": row[0], "name": row[1]})
    await database.disconnect()
    return JSONResponse(content={"person": formatted_result}, status_code=200)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)