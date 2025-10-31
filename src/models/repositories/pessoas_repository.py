from src.models.entities.pessoas import PESSOA
from src.models.settings.db_connection_handler import db_connection_handler as connection

class PessoasRepository:
    def __init__(self):
        self.__connection = connection.get_db_connection()

    def create(self, name):
        query = PESSOA.insert().values(name=name)
        self.db.execute(query)

    async def get_all_people(self):
        query = PESSOA.select()
        result = await self.__connection.fetch_all(query)
        return result
        

    def update(self, id, name):
        query = PESSOA.update().values(name=name).where(PESSOA.c.id == id)
        self.db.execute(query)

    def delete(self, id):
        query = PESSOA.delete().where(PESSOA.c.id == id)
        self.db.execute(query)