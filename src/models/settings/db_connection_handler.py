from databases import Database

class DBConnectionHandler:
    def __init__(self) -> None:
        self.__connection_string = "sqlite:///./schema.db"
        self.__database = Database(self.__connection_string)

    async def open_connection(self):
        await self.__database.connect()
        return self.__database

    async def close_connection(self):
        await self.__database.disconnect()

    def get_db_connection(self):
        return self.__database

db_connection_handler = DBConnectionHandler()