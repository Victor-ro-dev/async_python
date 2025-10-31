from src.controllers.pessoa_finder import PessoaFinder
from src.models.settings.db_connection_handler import db_connection_handler

class PessoasFinderView:
    def __init__(self):
        self.controller = PessoaFinder()

    async def handle_find_people(self, http_request = None) -> dict:
        response = await self.controller.find_all()
        http_request = {
            'status': 200,
            'body': response
        }
        return http_request