from fastapi import FastAPI
import uvicorn
import asyncio

app = FastAPI()

@app.get("/")
async def root():
    await asyncio.sleep(20)
    return {"message": "Hello World"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, workers=1)