from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.main.routes.pessoas_routes import pessoas_router

app = FastAPI()
app.include_router(pessoas_router)
