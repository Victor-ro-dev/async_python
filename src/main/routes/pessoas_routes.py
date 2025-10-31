from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from src.models.settings.db_connection_handler import db_connection_handler
from src.views.pessoas_finder_views import PessoasFinderView

pessoas_router = APIRouter()

@pessoas_router.get("/pessoas")
async def get_pessoas(resquet: Request):
    pessoas = PessoasFinderView()
    await db_connection_handler.open_connection()
    response = await pessoas.handle_find_people()
    await db_connection_handler.close_connection()          

    return JSONResponse(
        status_code=response['status'],
        content=response['body']
    )
    
